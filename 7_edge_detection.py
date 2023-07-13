import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale
def plot_image(image, title=""):
    pylab.title(title, size=10)
    pylab.imshow(image) 
    pylab.axis('off')
def plot_hist(r,g,b,title=""):
    r,g,b=r.astype(np.uint8),g.astype(np.uint8),b.astype(np.uint8) 
    pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
    pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
    pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
    pylab.xlabel('Pixel Values', size=20) 
    pylab.ylabel('Frequency',size=20)
    pylab.title(title,size=10)
# Edge Detectors with scikit-image-Prewitt, roberts, sobel, scharr, laplace 
im=Image.open("bird.jpg").convert('L')
im_arr=np.asarray(im)
pylab.gray() 
pylab.figure(figsize=(15,15))
pylab.subplot(3,2,1), plot_image(im,'Original Image') 
edges=filters.roberts(im_arr)
pylab.subplot(3,2,2), plot_image(edges,'Roberts')
edges=filters.scharr(im_arr)
pylab.subplot(3,2,3), plot_image(edges,'Scharr')
edges=filters.sobel(im_arr)
pylab.subplot(3,2,4), plot_image(edges,'Sobel')
edges=filters.prewitt(im_arr)
pylab.subplot(3,2,5), plot_image(edges,'Prewitt')
edges=np.clip(filters.laplace(im_arr), 0,1) 
pylab.subplot(3,2,6), plot_image(edges,'Laplace') 
pylab.subplots_adjust(wspace=0.1,hspace=0.1) 
pylab.show()