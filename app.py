import src.arguments as ah
from src.algorithms.runner import AlgorithmRunner

def main():
  arg_handler = ah.ArgumentHandler()

  algorithm = arg_handler.get_algorithm()
  image     = arg_handler.get_image()
  path      = arg_handler.get_path()

  ar = AlgorithmRunner(algorithm, image, path)
  ar.run()

if __name__ == "__main__":
  main()