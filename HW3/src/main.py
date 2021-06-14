import sys

from data import Data


# argv[1] : path tp samples file
def main(argv):
    path = argv[1]
    samples = Data(path).create_samples()




if __name__ == '__main__':
    main(sys.argv)
