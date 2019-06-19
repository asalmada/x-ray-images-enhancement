import numpy as np

def normalize(min_old, max_old, min_new, max_new, val):
	'''Normalizes values to the interval [min_new, max_new]

	Parameters:
		min_old: min value from old base.
		max_old: max value from old base.
		min_new: min value from new base.
		max_new: max value from new base.
		val: float or array-like value to be normalized.
	'''

	ratio = (val - min_old) / (max_old - min_old)
	normalized = (max_new - min_new) * ratio + min_new
	return normalized.astype(np.uint8)

def histogram(data):
	'''Generates the histogram for the given data.

	Parameters:
		data: data to make the histogram.

	Returns: histogram, bins.
	'''

	bins = np.sort(np.unique(data))
	data = data.flatten()
	hist = {}

	for b in bins:
		hist[b] = 0

	for pixel in data:
		hist[pixel] += 1

	bins_list = []
	hist_list = []
	for b in bins:
		bins_list.append(b)
		hist_list.append(hist[b])

	return np.array(hist_list), np.array(bins_list)

def to_grayscale(image):
	red_v = image[:, :, 0] * 0.299
	green_v = image[:, :, 1] * 0.587
	blue_v = image[:, :, 2] * 0.144
	image = red_v + green_v + blue_v

	return image.astype(np.uint8)