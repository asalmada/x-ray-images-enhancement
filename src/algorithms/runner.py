class AlgorithmRunner:
  def __init__(self, algorithm, image, path):
    self.__algorithm  = algorithm
    self.__image      = image
    self.__path       = path

  def __del__(self):
    self.__algorithm  = ''
    self.__image      = ''
    self.__path       = ''

  def run(self):
    '''Runs the algorithm for the image or images.'''
    pass