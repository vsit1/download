import cv2
import numpy as np
import matplotlib.pyplot as plt
# Open the image.
img = cv2.imread("flower.jpg")
# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)
# Save the output.
cv2.imwrite("flower1.jpg", log_transformed)
plt.imshow(img)
plt.show()
plt.imshow(log_transformed)
plt.show()
