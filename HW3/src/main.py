import sys

from data import Data
from agglomerative_clustering import AgglomerativeClustering
from link import *


# argv[1] : path tp samples file
def main(argv):
    path = argv[1]
    samples = Data(path).create_samples()

    single_link = SingleLink()
    print("single link:")
    agglomerate = AgglomerativeClustering(single_link, samples)
    agglomerate.run(7)

    print("")
    complete_link = CompleteLink()
    print("complete link:")
    agglomerate = AgglomerativeClustering(complete_link, samples)
    agglomerate.run(7)


if __name__ == '__main__':
    main(sys.argv)
