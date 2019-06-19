#High-frequency Emphasis filtering algorithm

import numpy as np
from scipy.fftpack import fft, ifft, fftshift
import imageio
from matplotlib import pyplot as plt

from .base import BaseAlgorithm


class HEF(BaseAlgorithm):
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        '''Runs the algorithm for the image.'''
        image = imageio.imread(self.filename)
        m = image.shape[0]
        n = image.shape[1]
        blurred_image = np.zeros((m, n))
        if len(image.shape) == 3:
            for i in range(m):
                for j in range(n):
                    red_v = image[i][j][0] * 0.299
                    green_v = image[i][j][1] * 0.587
                    blue_v = image[i][j][2] * 0.144
                    blurred_image[i][j] = red_v + green_v + blue_v

        fftimg = fft(blurred_image)
        sfftimg = fftshift(fftimg)
        m, n = sfftimg.shape
        H = np.zeros((m, n))
        D0 = 40
        for i in range(m):
            for j in range(n):
                H[i, j] = 1.0 - np.exp(
                    - ((i - m / 2.0) ** 2 + (j - n / 2.0) ** 2) / (
                                2 * (D0 ** 2)))
        k1 = 0.5
        k2 = 0.75
        filter = k1 + k2 * H

        HFE = np.multiply(filter, sfftimg)

        HFE = ifft(HFE)

        imax = np.max(HFE)
        imin = np.min(HFE)
        HFE = (HFE - imin) / (imax - imin)
        HFE = HFE * np.max(image)
        image = HFE

        plt.imshow(blurred_image, cmap="gray")
        plt.show()
        plt.imshow(image)
        plt.show()

        return image
