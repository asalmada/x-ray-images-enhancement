from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
	'''Class that must be inherited for each algorithm.'''

	@abstractmethod
	def __init__(self, filename, results_path):
		raise NotImplementedError

	@abstractmethod
	def run(self):
		'''Runs the algorithm, returning an image normalized to [0, 255].'''
		raise NotImplementedError

	@abstractmethod
	def get_input(self):
		'''Receives the input for the algorithm. It can be any variable, like window size in CLAHE.'''
		raise NotImplementedError