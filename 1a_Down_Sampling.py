import os
os.sys.path 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
img1 = cv2.imread('flower.jpg',0) 
[m, n] = img1.shape 
print('Image Shape:', m, n) 
print('Original Image:') 
plt.imshow(img1, cmap="gray") 
plt.show()
f = 4
img2 = np.zeros((m//f, n//f), dtype=np.int_)
for i in range(0, m, f): 
    for j in range(0, n, f): 
        try: 
            img2[i//f][j//f] = img1[i][j] 
        except IndexError: 
            pass 
print('Down Sampled Image:') 
plt.imshow(img2, cmap="gray")
plt.show()
