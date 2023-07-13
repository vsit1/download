import cv2
import numpy as np
import matplotlib.pyplot as plt
# Open the image.
img = cv2.imread("flower.jpg")
plt.imshow(img)
plt.show()
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2,5]:
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    # Save edited images.
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
    plt.imshow(gamma_corrected)
    plt.show()
