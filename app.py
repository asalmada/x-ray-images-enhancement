import src.arguments as ah
import src.algorithms.runner as ar

def main():
  arg_handler = ah.ArgumentHandler()

  algorithm = arg_handler.get_algorithm()
  image     = arg_handler.get_image()
  path      = arg_handler.get_path()

  algorithm_runner = ar.AlgorithmRunner(algorithm, image, path)
  algorithm_runner.run()

if __name__ == "__main__":
  main()