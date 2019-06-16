from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
	'''Class that must be inherited for each algorithm.'''

	@abstractmethod
	def __init__(self, filename):
		raise NotImplementedError

	@abstractmethod
	def run(self):
		raise NotImplementedError