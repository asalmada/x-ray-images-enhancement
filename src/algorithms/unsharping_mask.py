import imageio
import numpy as np
from scipy.ndimage.filters import gaussian_filter
from skimage import img_as_float

from .base import BaseAlgorithm

class UM(BaseAlgorithm):
	def __init__(self, filename):
		self.filename = filename

	def run(self):

		radius = 5
		amount = 2

		image = imageio.imread(self.filename)
		image = img_as_float(image) # ensuring float values for computations

		blurred_image = gaussian_filter(image, sigma=radius)
		mask = image - blurred_image # keep the edges created by the blur
		sharpened_image = image + mask * amount

		sharpened_image = np.clip(sharpened_image, float(0), float(1)) # Interval [0.0, 1.0]
		sharpened_image = (sharpened_image*255).astype(np.uint8) # Interval [0,255]

		return sharpened_image