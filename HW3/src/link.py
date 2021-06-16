import abc


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):
        pass


class SingleLink(Link):
    """
    Returns distance between two clusters according to the SingleLink method
    """
    def compute(self, cluster, other):
        min_ = cluster.samples[0].compute_euclidean_distance(other.samples[0])
        for cluster_sample in cluster.samples:
            for other_samples in other.samples:
                tmp_distance = cluster_sample.compute_euclidean_distance(other_samples)
                if min_ > tmp_distance:
                    min_ = tmp_distance
        return min_


class CompleteLink(Link):
    """
    Returns distance between two clusters according to the CompleteLink method
    """
    def compute(self, cluster, other):
        max_ = cluster.samples[0].compute_euclidean_distance(other.samples[0])
        for cluster_sample in cluster.samples:
            for other_samples in other.samples:
                tmp_distance = cluster_sample.compute_euclidean_distance(other_samples)
                if max_ < tmp_distance:
                    max_ = tmp_distance
        return max_
