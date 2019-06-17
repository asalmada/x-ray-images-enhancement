import os
import imageio

from datetime import datetime

import src.arguments as ah

from src.algorithms.unsharping_mask import UM

class AlgorithmRunner:
	def __init__(self):
		self.arg_handler	= ah.ArgumentHandler()
		self.algorithm		= self.arg_handler.get_algorithm()
		self.image				= self.arg_handler.get_image()
		self.images_path	= self.arg_handler.get_path()
		self.results_path	= os.path.join("results", str(datetime.now()))

		os.makedirs(self.results_path, exist_ok=True)

	def __del__(self):
		self.algorithm		= ''
		self.image				= ''
		self.images_path	= ''
		self.results_path	= ''

	def run(self):
		'''Runs the algorithm in the images.'''

		if self.images_path:
			images = os.listdir(self.images_path)
			path = self.images_path
		else:
			# We put in a list to be able to utilize the for loop
			images = [self.image]
			path = ""

		for image in images:
			split_image = image.split('/')
			if len(split_image) != 1:
				self.image = split_image[-1]
			else:
				self.image = image

			processed_image = self.__run_algorithm(image, path)
			imageio.imwrite(os.path.join(self.results_path, self.image), processed_image)

	def __run_algorithm(self, image, path):
		'''Runs the algorithm in the image.

		Parameters:
			image: image filename.
			path: image directory.

		Returns the processed image.
		'''

		img = os.path.join(path, image)

		# UM (Unsharping Mask)
		if self.algorithm == 'um':
			alg = UM(img)
		# TODO: HEF
		# TODO: N-CLAHE

		image = alg.run()

		return image