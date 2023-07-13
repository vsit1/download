import numpy as np
from PIL import Image
def signaltonoise(a, axis=0, ddof=0):
 a = np.asanyarray(a)
 m = a.mean(axis)
 sd = a.std(axis=axis, ddof=ddof)
 return np.where(sd == 0, 0, m/sd)
from scipy.fftpack import fft2, ifft2
#from scipy.stats import signaltonoise
import matplotlib.pyplot as plt
im = np.array(Image.open("flower.jpg").convert('L'))
freq = fft2(im)
im1 = ifft2(freq).real
snr = signaltonoise(im1, axis=None)
print('SNR FOR THE IMAGE OBTAINED AFTER RECONSTRUCTION = ' + str(snr))
assert(np.allclose(im, im1))
plt.figure(figsize=(20,10))
plt.subplot(121)
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.title('ORIGINAL IMAGE', size=20)
plt.subplot(122)
plt.imshow(im1, cmap='gray')
plt.axis('off')
plt.title('IMAGE OBTAINED AFTER RECONSTRUCTION', size=20)
plt.show()
