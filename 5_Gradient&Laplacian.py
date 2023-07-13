#GRADIENT
import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float, img_as_ubyte
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale
def plot_image(image, title=""):
    pylab.title(title, size=20),
    pylab.imshow(image) 
    pylab.axis('off')
def plot_hist(r,g,b,title=""):
    r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
    pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
    pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
    pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
    pylab.xlabel('Pixel Values', size=20) 
    pylab.ylabel('Frequency',size=20)
    pylab.title(title,size=10)
ker_x=[[-1,1]]
ker_y=[[-1],[1]] 
im=rgb2gray(imread("flower.jpg")) 
im_x=signal.convolve2d(im,ker_x,mode='same') 
im_y=signal.convolve2d(im,ker_y,mode='same')
im_mag=np.sqrt(im_x**2+im_y**2) 
im_dir=np.arctan(im_y/im_x)
pylab.gray() 
pylab.figure(figsize=(30,20))
pylab.subplot(231)
plot_image(im,'Original') 
pylab.subplot(232) 
plot_image(im_x,'Gradian_x') 
pylab.subplot(233) 
plot_image(im_y,'Grad+y') 
pylab.subplot(234)
plot_image(im_mag,'||grad||') 
pylab.subplot(235) 
plot_image(im_dir, r'$\theta$') 
pylab.subplot(236)
pylab.plot(range(im.shape[1]), im[0,:], 'b-', label=r'$f(x,y)|_{x=0}$', 
linewidth=5)
pylab.plot(range(im.shape[1]), im_x[0,:], 'r-', label=r'$grad_x (f(x,y))|_{x=0}$') 
pylab.title(r'$grad_x (f(x,y))|_{x=0}$',size=30)
pylab.legend(prop={'size':20})
pylab.show()
#LAPLACIAN
ker_laplacian=[[0,-1,0],[-1,4,-1],[0,-1,0]]
im=rgb2gray(imread("flower.jpg")) 
im1=np.clip(signal.convolve2d(im, ker_laplacian, mode='same'),0,1) 
pylab.gray()
pylab.figure(figsize=(20,10)) 
pylab.subplot(121)
plot_image(im, 'Original')
pylab.subplot(122)
plot_image(im1,'laplacian Convolved') 
pylab.show()