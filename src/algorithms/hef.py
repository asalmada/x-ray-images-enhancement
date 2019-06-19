#High-frequency Emphasis filtering algorithm

import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio
from matplotlib import pyplot as plt

from .base import BaseAlgorithm
import src.utils as pu


class HEF(BaseAlgorithm):
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        '''Runs the algorithm for the image.'''
        image = imageio.imread(self.filename)
        m = image.shape[0]
        n = image.shape[1]

        if len(image.shape) == 3:
            blurred_image = pu.to_grayscale(image)

        fftimg = fft2(blurred_image)
        sfftimg = fftshift(fftimg)

        m, n = sfftimg.shape
        H = np.zeros((m, n))
        D0 = 40
        for i in range(m):
            for j in range(n):
                H[i, j] = 1.0 - np.exp(- ((i - m / 2.0) ** 2 + (j - n / 2.0) ** 2) / (2 * (D0 ** 2)))
        k1 = 0.5
        k2 = 0.75
        filter = k1 + k2 * H

        shfe = filter * sfftimg
        hfe = np.real(ifft2(fftshift(shfe)))

        image_histogram, bins = np.histogram(hfe.flatten(), 256,
                                             density=True)

        cdf = image_histogram.cumsum()
        cdf = 255 * cdf / cdf[-1]
        image_equalized = np.interp(hfe.flatten(), bins[:-1], cdf)

        image = image_equalized.reshape(hfe.shape)

        # plt.subplot(121)
        # plt.imshow(blurred_image, cmap="gray")
        # plt.title('original image')
        # plt.axis('off')
        # plt.subplot(122)
        # plt.imshow(image, cmap="gray")
        # plt.title('High-frequency Emphasis')
        # plt.axis('off')
        # plt.show()

        return image.astype(np.uint8)
