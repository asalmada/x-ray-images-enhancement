import imageio
import numpy as np
from scipy.ndimage.filters import gaussian_filter, median_filter, maximum_filter, minimum_filter
from skimage import img_as_float

from .base import BaseAlgorithm

class UM(BaseAlgorithm):
	def __init__(self, filename):
		self.filename = filename
		self.get_input()

	def get_input(self):
		print("Select filter (1 - Gaussian, 2  - Median, 3 - Maximum, 4 - Minimum): ")
		self.filter = int(input())

		if self.filter == 1: # Gaussian filter specific
			print("Select value for radius: ")
			self.radius = int(input())
		
		print("Select value for amount: ")
		self.amount = int(input())

	def run(self):

		#radius = 5
		#amount = 2

		image = imageio.imread(self.filename)
		image = img_as_float(image) # ensuring float values for computations

		if self.filter == 1:
			blurred_image = gaussian_filter(image, sigma=self.radius)
		elif self.filter == 2:
			blurred_image = median_filter(image, size=20)
		elif self.filter == 3:
			blurred_image = maximum_filter(image, size=20)
		else:
			blurred_image = minimum_filter(image, size=20)

		mask = image - blurred_image # keep the edges created by the filter
		sharpened_image = image + mask * self.amount

		sharpened_image = np.clip(sharpened_image, float(0), float(1)) # Interval [0.0, 1.0]
		sharpened_image = (sharpened_image*255).astype(np.uint8) # Interval [0,255]

		return sharpened_image