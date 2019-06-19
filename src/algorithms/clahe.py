from src.algorithms.base import BaseAlgorithm
import src.utils as pu

import numpy as np
import imageio

from collections import Counter

class CLAHE(BaseAlgorithm):
	'''Contrast Limited Adaptive Histogram Equalization'''

	def __init__(self, filename):
		self.filename = filename

	def run(self):
		image = imageio.imread(self.filename)

		if len(image.shape) > 2:
			image = pu.to_grayscale(image)

		shape = image.shape
		normalized_image = pu.normalize(np.min(image), np.max(image), 0, 255, image)

		window_size = 20
		clip_limit = 20

		equalized_image = self.clahe(normalized_image, window_size, clip_limit)

		return equalized_image

	def clahe(self, image, window_size, clip_limit):
		'''Applies the CLAHE algorithm in an image.

		Parameters:
			image: image to be processed.
			window_size: size of the window used to calculate the transform function.
			clip_limit: histogram clipping limit.

		Returns a processed image.
		'''

		border = window_size // 2
		max_val = 255
		padded_image = np.pad(image, border, "reflect")
		shape = padded_image.shape
		padded_equalized_image = np.zeros(shape).astype(np.uint8)

		for i in range(border, shape[0] - border):
			for j in range(border, shape[1] - border):
				# Region to extract the histogram
				region = padded_image[i-border:i+border+1, j-border:j+border+1]
				# Calculating the histogram from region
				clipped_hist = self.clipped_histogram_equalization(region, max_val, clip_limit)
				# Changing the value of the image to the result from the CDF for the given pixel
				padded_equalized_image[i][j] = clipped_hist[padded_image[i][j]]

		# Removing the padding from the image
		equalized_image = padded_equalized_image[border:shape[0] - border, border:shape[1] - border].astype(np.uint8)

		return equalized_image

	def clipped_histogram_equalization(self, region, max_val, clip_limit):
		'''Calculates the clipped histogram equalization for the given region.

		Parameters:
			region: array-like.
			max_val: max value for the image
			clip_limit: max value for a pixel in the histogram.

		Returns a dictionary with the CDF for each pixel in the region.
		'''

		# Building the histogram
		hist, bins = pu.histogram(region)
		n_bins = len(bins)

		# Removing values above clip_limit
		excess = 0
		for i in range(n_bins):
			if hist[i] > clip_limit:
				excess += hist[i] - clip_limit
				hist[i] = clip_limit

		## Redistributing exceding values ##
		# Calculating the values to be put on all bins
		for_each_bin = excess // n_bins
		# Calculating the values left
		leftover = excess % n_bins

		hist += for_each_bin
		for i in range(leftover):
			hist[i] += 1

		# Calculating probability for each pixel
		pixel_probability = hist / hist.sum()
		# Calculating the CDF (Cumulative Distribution Function)
		cdf = np.cumsum(pixel_probability)

		cdf_normalized = cdf * max_val

		hist_eq = {}
		for i in range(len(cdf)):
			hist_eq[bins[i]] = int(cdf_normalized[i])

		return hist_eq