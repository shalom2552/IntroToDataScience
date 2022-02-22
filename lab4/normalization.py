from point import Point
from numpy import mean, var


class DummyNormalizer:
    def fit(self, points):
        pass

    def transform(self, points):
        return points


class ZNormalizer:
    def __init__(self):
        self.mean_variance_list = []

    def fit(self, points):
        all_coordinates = [p.coordinates for p in points]
        self.mean_variance_list = []
        for i in range(len(all_coordinates[0])):
            values = [x[i] for x in all_coordinates]
            self.mean_variance_list.append([mean(values), var(values, ddof=1)**0.5])

    def transform(self, points):
        new = []
        for p in points:
            new_coordinates = p.coordinates
            new_coordinates = [(new_coordinates[i] - self.mean_variance_list[i][0]) / self.mean_variance_list[i][1]
                               for i in range(len(p.coordinates))]
            new.append(Point(p.name, new_coordinates, p.label))
        return new


class SumNormalizer:
    def __init__(self):
        self.sums = []

    def fit(self, points):
        for i in range(len(points[0].coordinates)):
            sum_ = 0
            for point in points:
                sum_ += abs(point.coordinates[i])
            self.sums.append(sum_)

    def transform(self, points):
        transformed_points = []
        for point in points:
            new_coordinate = []
            for i in range(len(point.coordinates)):
                new_coordinate.append(point.coordinates[i]/self.sums[i])
            transformed_points.append(Point(point.name, new_coordinate, point.label))
        return transformed_points


class MinMaxNormalizer:
    def __init__(self):
        self.min = []
        self.max = []

    def fit(self, points):
        for i in range(len(points[0].coordinates)):
            min_ = points[0].coordinates[i]
            max_ = points[0].coordinates[i]
            for point in points:
                if point.coordinates[i] >= max_:
                    max_ = point.coordinates[i]
                if point.coordinates[i] <= min_:
                    min_ = point.coordinates[i]
            self.min.append(min_)
            self.max.append(max_)

    def transform(self, points):
        transformed_points = []
        for point in points:
            new_coordinate = []
            for i in range(len(point.coordinates)):
                new_coordinate.append((point.coordinates[i] - self.min[i]) / (self.max[i] - self.min[i]))
            transformed_points.append(Point(point.name, new_coordinate, point.label))
        return transformed_points

