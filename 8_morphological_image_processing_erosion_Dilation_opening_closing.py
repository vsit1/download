import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.morphology import binary_opening, binary_closing, disk
from skimage.color import rgb2gray
from skimage.io import imread
import matplotlib.pylab as pylab
def plot_image(image, title=""):
    pylab.title(title, size=10)
    pylab.imshow(image)
    pylab.axis('off')
# Erosion and Dilation
img = cv2.imread("bird.jpg", 0)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap="gray")
plt.axis('off')
plt.title("ORIGINAL IMAGE")
plt.show()
plt.figure(figsize=(5, 5))
plt.imshow(img_erosion)
plt.axis('off')
plt.title("EROSION")
plt.show()
plt.figure(figsize=(5, 5))
plt.imshow(img_dilation, cmap="gray")
plt.axis('off')
plt.title("DILATION")
plt.show()
# Image opening and closing
im = rgb2gray(imread("bird.jpg"))
im[im <= 0.5] = 0
im[im > 0.5] = 1
pylab.gray()
pylab.figure(figsize=(20, 10))
pylab.subplot(1, 3, 1), plot_image(im, 'original')
im1 = binary_opening(im, disk(6))
pylab.subplot(1, 3, 2), plot_image(im1, 'opening with disk size ' + str(10))
im1 = binary_closing(im, disk(6))
pylab.subplot(1, 3, 3), plot_image(im1, 'closing with disk size ' + str(6))
pylab.show()