#High-frequency Emphasis filtering algorithm

import numpy as np
from scipy.fftpack import fft, ifft, fftshift
import imageio

filename = str(input()).rstrip()
img = imageio.imread(filename)
print(img.shape)
fftimg = fft(img)
print(fftimg.shape)
sfftimg = fftshift(fftimg)
print(sfftimg.shape)
m, n= sfftimg.shape
H = np.zeros((m, n))
# H[2] = img[2]
D0 = 40
for i in range(m):
    for j in range(n):
        H[i, j] = 1.0 - np.exp(- ((i - m / 2.0) ** 2 + (j - n / 2.0) ** 2) / (2 * (D0 ** 2)))
k1 = 0.5
k2 = 0.75
filter = k1 + k2 * H

HFE = np.multiply(filter, sfftimg)

HFE = ifft(HFE)

imax = np.max(HFE)
imin = np.min(HFE)
HFE = (HFE - imin) / (imax - imin)
HFE = HFE * np.max(img)
print(HFE.shape)
outputfilename = filename[:-4]+ "-HEF" + filename[-4:]
print(outputfilename)
imageio.imwrite(outputfilename, HFE)