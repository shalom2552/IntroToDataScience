import sys
import os
from cross_validation import CrossValidation
from knn import KNN
from metrics import accuracy_score
from normalization import *


def load_data(argv):
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


def run_1nn(points):
    m = KNN(1)
    m.train(points)
    predicts = []
    real = []
    for point in points:
        predicts.append(m.predict(point)[0])
        real.append(point.label)
    print(accuracy_score(real, predicts))


def run_knn_kpoints(points, k):
    m = KNN(k)
    sum_ = 0
    for _ in range(len(points)):
        point = points[0]
        points.remove(point)
        m.train(points)
        cl = m.predict(point)
        sum_ += accuracy_score(point.label, cl)
        points.append(point)
    return sum_/len(points)


def question_2(points):
    max_ = 0
    max_k = 0
    for i in range(1, 31):
        current = run_knn_kpoints(points, i)
        if current > max_:
            max_ = current
            max_k = i
    return max_k


def question_3(points, k):
    m = KNN(k)
    m.train(points)
    cv = CrossValidation()
    print("Question 3:")
    print("K=" + str(k))
    print("2-fold-cross-validation:")
    cv.run_cv(points, 2, m, accuracy_score, False, True)
    print("10-fold-cross-validation:")
    cv.run_cv(points, 10, m, accuracy_score, False, True)
    print("20-fold-cross-validation:")
    cv.run_cv(points, 20, m, accuracy_score, False, True)


def question_4(points, normalizers):
    print("Question 4:")
    m = KNN(5)
    m.train(points)
    cv = CrossValidation()
    print("K=5")
    for key in normalizers.keys():
        norm = normalizers.get(key)
        n = norm()
        n.fit(points)
        new_points = n.transform(points)
        print(f"Accuracy of {key} is " + str(cv.run_cv(new_points, 2, m, accuracy_score, False, True)))
        print("")
    m = KNN(7)
    m.train(points)
    print("K=7")
    for key in normalizers.keys():
        norm = normalizers.get(key)
        n = norm()
        n.fit(points)
        new_points = n.transform(points)
        print(f"Accuracy of {key} is " + str(cv.run_cv(new_points, 2, m, accuracy_score, False, True)))
        print("")


if __name__ == '__main__':
    loaded_points = load_data(sys.argv)
    k = question_2(loaded_points)
    question_3(loaded_points, k)
    question_4(loaded_points, {"DummyNormalizer": DummyNormalizer, "SumNormalizer": SumNormalizer,
                               "MinMaxNormalizer": MinMaxNormalizer, "ZNormalizer": ZNormalizer})
