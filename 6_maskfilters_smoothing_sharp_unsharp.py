import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float, img_as_ubyte 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale
def plot_hist(r,g,b,title=""):
    r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
    pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
    pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
    pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
    pylab.xlabel('Pixel Values', size=20)
    pylab.ylabel('Frequency',size=20)
    pylab.title(title,size=10)
def plot_image(image, title=""):
    pylab.title(title, size=10)
    pylab.imshow(image) 
    pylab.axis('off')
# sharpening of images
from skimage.filters import laplace 
im=rgb2gray(imread("flower.jpg")) 
im1=np.clip(laplace(im)+im,0,1)
pylab.figure(figsize=(10,15))
pylab.subplot(121), plot_image(im, 'Original Image') 
pylab.subplot(122), plot_image(im1,'Sharpened Image') 
pylab.tight_layout()
pylab.show()
def rgb2gray(im):
    return np.clip(0.2989*im[...,0]+0.5870*im[...,1]+0.1140*im[...,2],0,1) 
im=rgb2gray(img_as_float(imread("flower.jpg"))) 
im_blurred=ndimage.gaussian_filter(im,3)
im_detail=np.clip(im-im_blurred,0,1) 
pylab.gray()
fig, axes=pylab.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(15,15)) 
axes=axes.ravel()
axes[0].set_title('Original Image',size=15)
axes[0].imshow(im) 
axes[1].set_title('Blurred Image, signam=5', size=15)
axes[1].imshow(im_blurred) 
axes[2].set_title('Detail Image', size=15) 
axes[2].imshow(im_detail)
alpha=[1, 5, 10] 
for i in range(3):
    im_sharp=np.clip(im+alpha[i]*im_detail,0,1) 
    axes[3+i].imshow(im_sharp)
    axes[3+i].set_title('Sharpened Image, alpha='+str(alpha[i]),size=15) 
for ax in axes:
    ax.axis('off') 
fig.tight_layout() 
pylab.show()
