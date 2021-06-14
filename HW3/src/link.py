import abc


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):
        pass


class SingleLink(Link):
    def compute(self, cluster, other):
        dists = []
        for cluster_sample in cluster.samples:
            for other_samples in other.samples:
                dists.append(cluster_sample.compute_euclidean_distance(other_samples))
        return min(dists)


class CompleteLink(Link):
    def compute(self, cluster, other):
        dists = []
        for cluster_sample in cluster.samples:
            for other_samples in other.samples:
                dists.append(cluster_sample.compute_euclidean_distance(other_samples))
        return max(dists)
