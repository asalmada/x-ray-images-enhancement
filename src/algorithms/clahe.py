from src.algorithms.base import BaseAlgorithm
import src.utils as pu

import numpy as np
import imageio
import matplotlib.pyplot as plt
import os
import timeit

from collections import Counter

class CLAHE(BaseAlgorithm):
	'''Contrast Limited Adaptive Histogram Equalization.
	In reality, we do a normalization before applying CLAHE, making it the N-CLAHE method, but in
	N-CLAHE the normalization is done using a log function, instead of a linear one, as we use here.
	'''

	def __init__(self, filename, results_path):
		self.filename = filename
		self.results_path = results_path
		self.get_input()

	def run(self):
		image = imageio.imread(self.filename)

		if len(image.shape) > 2:
			image = pu.to_grayscale(image)

		normalized_image = pu.normalize(np.min(image), np.max(image), 0, 255, image)
		imageio.imwrite(os.path.join(self.results_path, "normalized_image.jpg"), normalized_image)

		start = timeit.default_timer()
		equalized_image = self.clahe(normalized_image)
		stop = timeit.default_timer()

		self.export_histogram(image, normalized_image, equalized_image)
		self.export_run_info(stop - start)

		return equalized_image

	def get_input(self):
		print("Window size: ")
		self.window_size = int(input())
		print("Clip limit: ")
		self.clip_limit = int(input())
		print("Number of iterations: ")
		self.n_iter = int(input())

	def clahe(self, image):
		'''Applies the CLAHE algorithm in an image.

		Parameters:
			image: image to be processed.

		Returns a processed image.
		'''

		border = self.window_size // 2

		padded_image = np.pad(image, border, "reflect")
		shape = padded_image.shape
		padded_equalized_image = np.zeros(shape).astype(np.uint8)

		for i in range(border, shape[0] - border):
			if i % 50 == 0:
				print(f"Line: {i}")
			for j in range(border, shape[1] - border):
				# Region to extract the histogram
				region = padded_image[i-border:i+border+1, j-border:j+border+1]
				# Calculating the histogram from region
				hist, bins = pu.histogram(region)
				# Clipping the histogram
				clipped_hist = pu.clip_histogram(hist, bins, self.clip_limit)
				# Trying to reduce the values above clipping
				for _ in range(self.n_iter):
					clipped_hist = pu.clip_histogram(hist, bins, self.clip_limit)
				# Calculating the CDF
				cdf = pu.calculate_cdf(hist, bins)
				# Changing the value of the image to the result from the CDF for the given pixel
				padded_equalized_image[i][j] = cdf[padded_image[i][j]]

		# Removing the padding from the image
		equalized_image = padded_equalized_image[border:shape[0] - border, border:shape[1] - border].astype(np.uint8)

		return equalized_image

	def clipped_histogram_equalization(self, region):
		'''Calculates the clipped histogram equalization for the given region.

		Parameters:
			region: array-like.

		Returns a dictionary with the CDF for each pixel in the region.
		'''

		# Building the histogram
		hist, bins = pu.histogram(region)
		n_bins = len(bins)

		# Removing values above clip_limit
		excess = 0
		for i in range(n_bins):
			if hist[i] > self.clip_limit:
				excess += hist[i] - self.clip_limit
				hist[i] = self.clip_limit

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

		cdf_normalized = cdf * 255

		hist_eq = {}
		for i in range(len(cdf)):
			hist_eq[bins[i]] = int(cdf_normalized[i])

		return hist_eq

	def export_histogram(self, image, normalized, equalized):
		plt.xlabel("Pixel")
		plt.ylabel("Count")

		hist, bins = pu.histogram(image)
		plt.plot(bins, hist, label='Original Image')
		plt.legend()

		hist, bins = pu.histogram(normalized)
		plt.plot(bins, hist, label='Normalized Image')
		plt.legend()

		hist, bins = pu.histogram(equalized)
		plt.plot(bins, hist, label='CLAHE Result')
		plt.legend()
		plt.savefig(os.path.join(self.results_path, "histograms.jpg"))

	def export_run_info(self, runtime):
		with open(os.path.join(self.results_path, "runinfo.txt"), 'w+') as f:
			f.write(f"Runtime: {runtime:.2f}s\n")
			f.write(f"Window size: {self.window_size}\n")
			f.write(f"Clip limit: {self.clip_limit}\n")