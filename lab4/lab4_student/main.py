from sys import argv
import os
from cross_validation import CrossValidation
from knn import KNN
from metrics import accuracy_score
from normalization import *


def load_data():
    """
    Loads data from path in first argument
    :return: returns data as list of Point
    """
    if len(argv) < 2:
        print('Not enough arguments provided. Please provide the path to the input file')
        exit(1)
    input_path = argv[1]

    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)

    points = []
    with open(input_path, 'r') as f:
        for index, row in enumerate(f.readlines()):
            row = row.strip()
            values = row.split(',')
            points.append(Point(str(index), values[:-1], values[-1]))
    return points


def run_knn(points):
    m = KNN(5)
    m.train(points)
    print(f'predicted class: {m.predict(points[0])}')
    print(f'true class: {points[0].label}')
    cv = CrossValidation()
    cv.run_cv(points, 10, m, accuracy_score)


if __name__ == '__main__':
    loaded_points = load_data()
    run_knn(loaded_points)
