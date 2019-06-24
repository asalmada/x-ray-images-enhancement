import argparse

class ArgumentHandler:
	'''Handles the program's arguments.'''

	def __init__(self):
		self.__parser = argparse.ArgumentParser()
		self.__define_arguments()
		self.__parsed_args = vars(self.__parser.parse_args())

	def __define_arguments(self):
		group = self.__parser.add_mutually_exclusive_group(required=True)
		group.add_argument("-i", metavar="img", type=str, help="image to be processed")
		group.add_argument("-p", metavar="path", type=str, help="path to the images to be processed")

		self.__parser.add_argument("-a", metavar="alg", type=str, help="algorithm to be used", required=True, choices=["clahe", "um", "hef"])
		self.__parser.add_argument("-o", metavar="path", type=str, help="path to export the results", required=False)

	def get_image(self):
		'''Gets the image from argument -i.'''

		if self.__parsed_args['i']:
			return self.__parsed_args['i']

	def get_path(self):
		'''Gets the path from argument -p.'''

		if self.__parsed_args['p']:
			return self.__parsed_args['p']

	def get_algorithm(self):
		'''Gets the algorithm from argument -a.'''

		return self.__parsed_args['a']

	def get_output_path(self):
		'''Gets the path from argument -o.'''

		if self.__parsed_args['o']:
			return self.__parsed_args['o']