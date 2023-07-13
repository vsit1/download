import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
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
#SOBEL
im=Image.open("bird.jpg").convert('L') 
im_array = np.asarray(im)
pylab.gray()
pylab.figure(figsize=(15,15)) 
pylab.subplot(2,2,1), plot_image(im,'Original')
pylab.subplot(2,2,2) 
edges_x=filters.sobel_h(im_array) 
plot_image(np.clip(edges_x,0,1),'sobel_x')
pylab.subplot(2,2,3) 
edges_y=filters.sobel_v(im_array) 
plot_image(np.clip(edges_y,0,1),'Sobel_y')
pylab.subplot(2,2,4) 
edges=filters.sobel(im_array) 
plot_image(np.clip(edges,0,1),'Sobel')
pylab.subplots_adjust(wspace=0.1,hspace=0.1)
pylab.show()
plt.show()
