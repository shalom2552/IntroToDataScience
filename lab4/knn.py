from collections import Counter


class KNN:
    def __init__(self, k=1, norm=2):
        """
        :param k: number of neighbors to consider
        :param norm: distance norm to use
        """
        self._points = []
        self._k = k
        self._norm = norm

    def reset(self, k=1, norm=2):
        """
        Resets classifier
        :param k: new k
        :param norm: new distance norm
        """
        self._points = []
        self._k = k
        self._norm = norm

    def train(self, training_points):
        """
        trains the model
        :param training_points: list of Point to use for training
        """
        self._points = list(training_points)

    def predict(self, testing_points):
        """
        Predicts labels for given test set
        :param testing_points: Point or List of Points
        :return: list of targets
        """
        if len(self._points) == 0:
            print('Please train the model first')
            return []
        if type(testing_points) != list:
            # In case single point is provided
            testing_points = [testing_points]
        result = [self._predict(x) for x in testing_points]
        return result

    def _predict(self, point):
        index_to_distance = {point_index: point.distance_to(p.coordinates)
                             for point_index, p in enumerate(self._points)}  # dict point_index -> distance
        sorted_indices = sorted(index_to_distance.keys(), key=lambda x: index_to_distance[x])
        closest_neighbors = [self._points[i] for i in sorted_indices[:self._k]]
        closest_targets = [p.label for p in closest_neighbors]

        counts = Counter(closest_targets)
        most_common = counts.most_common(1)[0][0]

        return most_common
