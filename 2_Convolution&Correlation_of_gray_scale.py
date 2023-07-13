import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(1, figsize=(12,8))
plt.imshow(image)
#plt.show()
abc=np.ones((3,3))
kernel = np.ones((3, 3), np.float32) / 9
img = cv2.filter2D(image, -1, kernel)
fig, ax = plt.subplots(1,2,figsize=(10,6))
ax[0].imshow(image)
ax[1].imshow(img)
#plt.show()
kernel = np.array([[0, -1, 0],
 [-1, 5, -1],
 [0, -1, 0]])
img = cv2.filter2D(image, -1, kernel)
fig, ax = plt.subplots(1,2,figsize=(10,6))
ax[0].imshow(image)
ax[1].imshow(img)
#plt.show()
