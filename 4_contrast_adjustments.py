import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import data, img_as_float, img_as_ubyte, exposure, io, color
from PIL import Image, ImageEnhance, ImageFilter
from scipy import ndimage, misc 
import matplotlib.pyplot as pylab 
import cv2
def plot_image(image, title=""):
    pylab.title(title, size=10) 
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
def contrast(c):
    return 0 if c<50 else (255 if c>150 else int((255*c-22950)/48))
im=Image.open("flower.jpg") 
im_r,im_g,im_b=im.split() 
pylab.style.use('ggplot')
pylab.figure(figsize=(15,5))
pylab.subplot(121) 
plot_image(im)
pylab.subplot(122)
plot_hist(im_r,im_g,im_b)
pylab.show()
imc=im.point(contrast) 
im_rc,im_gc,im_bc=imc.split() 
pylab.style.use('ggplot')
pylab.figure(figsize=(15,5))
pylab.subplot(121)
plot_image(imc) 
pylab.subplot(122) 
plot_hist(im_rc,im_gc,im_bc)
pylab.yscale('log')
pylab.show()