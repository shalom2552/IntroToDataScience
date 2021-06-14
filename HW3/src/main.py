import sys

from data import Data
from agglomerative_clustering import AgglomerativeClustering
from link import *


# argv[1] : path tp samples file
def main(argv):
    path = argv[1]
    samples = Data(path).create_samples()

    link = Link()

    agglomerative = AgglomerativeClustering(link, samples)
    print("__DEBUG__ Agglomerative init!")  # TODO debug
    agglomerative.run(7)


if __name__ == '__main__':
    main(sys.argv)
