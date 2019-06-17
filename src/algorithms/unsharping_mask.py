import cv2
import imageio
import numpy as np
from matplotlib import pyplot as plt

from .base import BaseAlgorithm

class UM(BaseAlgorithm):
	def __init__(self, filename):
		self.filename = filename

	def run(self):
		# https://stackoverflow.com/questions/2938162/how-does-an-unsharp-mask-work
		# https://en.wikipedia.org/wiki/Unsharp_masking
		image = imageio.imread(self.filename)
		n,m = image.shape[0], image.shape[1]
		weight = 0.8
		threshold = 190

		blurred_image = cv2.GaussianBlur(image,(7,7),0)
		mask = image - blurred_image

		# TODO Get another version of the image with
		# higher contrast to use in this operation
		for x in range(n):
				for y in range(m):
						new_value = weight * mask[x,y]

						if(np.all(new_value) > threshold):
								image[x,y] = image[x,y] + new_value

		# Debugging
		#plt.imshow(blurred_image, cmap="gray")
		#plt.show()
		plt.imshow(mask, cmap="gray")
		plt.show()
		plt.imshow(image, cmap="gray")
		plt.show()

		return image