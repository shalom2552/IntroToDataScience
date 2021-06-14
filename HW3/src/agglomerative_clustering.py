from collections import OrderedDict
from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        clusters = []
        for sample in samples:
            clusters.append(Cluster(sample.s_id, [sample]))
        self.clusters = clusters
        #print("**Debug** clusters:", self.clusters) TODO
        self.samples = samples
        pass

    def run(self, max_clusters):
        # run algorithm
        # TODO cluster have to be sorted
        print("single link:")
        i = 0
        for cluster in self.clusters:
            #silhouette = self.compute_silhouette()
            silhouette = 0  # TODO DEBUG
            cluster.print_details(silhouette)
            i += 1
            print("**DEBUG** run round:",i)
            if i == max_clusters:
                break
        pass

    """
    dictionary where all keys are identifiers of all data samples
    and the compatible value is the silhouette measure
    """
    def compute_silhouette(self):
        results = OrderedDict()
        for cluster in self.clusters:
            for x in cluster.samples:
                if len(cluster.samples) <= 1:
                    x_silhouette = 0
                else:
                    in_x = self.in_function(self, x)
                    out_x = self.out_function(self, x)
                    x_silhouette = (out_x - in_x)/max(out_x, in_x)
                results.update({x.s_id, x_silhouette})
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
        for s_id, x_silhouette in zip(silhouette):
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
        return (TP + TN)/(TP + TN + FP + FN) if (TP + TN + FP + FN) != 0 else 0

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
