from collections import OrderedDict
from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        clusters = []
        for sample in samples:
            clusters.append(Cluster(sample.s_id, [sample]))
        self.clusters = clusters
        self.samples = samples
        pass

    def run(self, max_clusters):
        # 1. compute similarity information between every pair of objects in the data set.
        # 2. merge cluster by link method
        # 3. Determining where to cut the hierarchical tree into clusters. This creates a partition of the data.
        # run algorithm
        cluster_count = len(self.clusters)
        tuple_list = []

        # as long as not reached max_cluster count, keep merging
        count = 0  # TODO DEBUG
        while cluster_count > max_clusters:
            # go over and find the closest cluster by link method
            count += 1  # TODO DEBUG
            print("**DEBUG** iteration of run in agg.. :", count)  # TODO DEBUG
            print("  cluster_count:", cluster_count)  # TODO DEBUG

            cluster_count = len(self.clusters)
            for i in range(cluster_count):
                for j in range(cluster_count):
                    if i == j:
                        continue
                    dists = self.link.compute(self.clusters[i], self.clusters[j])
                    tuple_list.append([i, j, dists])

            max_dist = [-1, -1, 0]
            for tuple_element in tuple_list:
                if max_dist[2] < tuple_element[2]:
                    max_dist = [tuple_element[0], tuple_element[1], tuple_element[2]]
                    print("  max_dist:", max_dist)  # TODO DEBUG

            # we found the closest cluster, now we need to merge them
            print("**DEBUG**  max dist:", max_dist)  # TODO DEBUG
            self.clusters[max_dist[0]].merge(self.clusters[max_dist[1]])
            # after we merged the second cluster into the first one, we delete the old merged one
            del self.clusters[max_dist[1]]

        # now we have 7 clusters in the list
        assert len(self.clusters) != max_clusters
        self.clusters.sort()
        silhouette = self.compute_summery_silhouette()
        for cluster in self.clusters:
            cluster_silhouette = silhouette[cluster.c_id]
            cluster.print_details(cluster_silhouette)

    """
    dictionary where all keys are identifiers of all data samples
    and the compatible value is the silhouette measure
    """
    def compute_silhouette(self):
        results = {}
        for cluster in self.clusters:
            for x in cluster.samples:
                if len(cluster.samples) <= 1:
                    x_silhouette = 0
                else:
                    in_x = self.in_function(self, x)
                    out_x = self.out_function(self, x)
                    x_silhouette = (out_x - in_x)/max(out_x, in_x)
                results[x.s_id] = x_silhouette  # .update({x.s_id, x_silhouette})
        return results

    """
    This method returns a dictionary that summarizes the silhouette index
    for the result of the cluster algorithm.
    :returns dictionary such that the keys are the cluster identifiers and another key 0
    :return 
    """
    def compute_summery_silhouette(self):
        total_silhouette, total_len = 0, 0
        summery_silhouette = OrderedDict()
        silhouette = self.compute_silhouette()
        for cluster in self.clusters:
            summery_silhouette[cluster.c_id] = 0
        for s_id, x_silhouette in silhouette.items():
            total_silhouette += x_silhouette
            found = False
            for cluster in self.clusters:
                if found:
                    break
                for sample in cluster.samples:
                    if s_id == sample.s_id:
                        summery_silhouette[cluster.c_id] += x_silhouette
                        found = True
                        break
        for cluster in self.clusters:
            len_cluster = len(cluster.samples)
            total_len += len_cluster
            summery_silhouette[cluster.c_id] /= len_cluster
        # sample silhouette
        summery_silhouette[0] = total_silhouette/total_len
        return summery_silhouette

    def compute_rand_index(self):
        TP, TN, FP, FN = 0, 0, 0, 0

        for sample_1 in self.samples:
            for sample_2 in self.samples:
                if sample_1.s_id == sample_2.s_id:
                    continue
                cluster_1, cluster_2 = self.get_cluster(sample_1), self.get_cluster(sample_2)
                label_1, label_2 = sample_1.label, sample_2.label
                if cluster_1 == cluster_2 and label_1 == label_2:
                    TP += 1
                elif cluster_1 != cluster_2 and label_1 != label_2:
                    TN += 1
                elif cluster_1 == cluster_2 and label_1 != label_2:
                    FP += 1
                elif cluster_1 != cluster_2 and label_1 == label_2:
                    FN += 1
        return (TP + TN)/(TP + TN + FP + FN)  # if (TP + TN + FP + FN) != 0 else 0

    def get_cluster(self, x):
        for cluster in self.clusters:
            for sample in cluster.samples:
                if sample.s_id == x.s_id:
                    return cluster.c_id
        pass

    @staticmethod
    def in_function(self, x):
        for cluster in self.clusters:
            if x in cluster:
                sum_dists = 0
                for point in cluster:
                    if point.s_id != x.s_id:
                        sum_dists += x.compute_euclidean_distance(point)
                return sum_dists/(len(cluster.samples) - 1)
            else:
                raise
        pass

    @staticmethod
    def out_function(self, x):
        cluster_dists = []
        for cluster in self.clusters:
            if x not in cluster.samples:
                sum_dist = 0
                for point in cluster.samples:
                    sum_dist += x.compute_euclidean_distance(point)
                cluster_dists.append(sum_dist/len(cluster.samples))
        return min(cluster_dists)
