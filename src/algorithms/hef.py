# High-frequency Emphasis filtering algorithm

import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio
from .base import BaseAlgorithm
import src.utils as pu


class HEF(BaseAlgorithm):
    def __init__(self, filename, results_path):
        self.filename = filename
        self.get_input()
        self.results_path = results_path

    def get_input(self):
        print(
            "Select D0 value for High cut (1 to 90): ")
        self.d0v = int(input())
        assert 1 <= self.d0v <= 90

    def run(self):
        '''Runs the algorithm for the image.'''
        image = imageio.imread(self.filename)

        if len(image.shape) == 3:
            img_grayscale = pu.to_grayscale(image)
        img = pu.normalize(np.min(img_grayscale), np.max(image), 0, 255,
                                        img_grayscale)
        # HF part
        img_fft = fft2(img)  # img after fourier transformation
        img_sfft = fftshift(img_fft)  # img after shifting component to the center

        m, n = img_sfft.shape
        filter_array = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                filter_array[i, j] = 1.0 - np.exp(- ((i-m / 2.0) ** 2 + (j-n / 2.0) ** 2) / (2 * (self.d0v ** 2)))
        k1 = 0.5
        k2 = 0.75
        high_filter = k1 + k2*filter_array

        img_filtered = high_filter * img_sfft
        img_hef = np.real(ifft2(fftshift(img_filtered)))  # HFE filtering done

        # HE part
        # Building the histogram
        hist, bins = pu.histogram(img_hef)
        # Calculating probability for each pixel
        pixel_probability = hist / hist.sum()
        # Calculating the CDF (Cumulative Distribution Function)
        cdf = np.cumsum(pixel_probability)
        cdf_normalized = cdf * 255
        hist_eq = {}
        for i in range(len(cdf)):
            hist_eq[bins[i]] = int(cdf_normalized[i])

        for i in range(m):
            for j in range(n):
                image[i][j] = hist_eq[img_hef[i][j]]

        return image.astype(np.uint8)
