

class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    """
    Given a cluster the function will merge it into the current cluster.
    :param other: cluster to be merge to 
    """
    def merge(self, other):  # TODO implement!!
        self.c_id = min(self.c_id, other.c_id)
        self.samples = self.samples + other.samples

    """
    print cluster data:
    1. id of points in ascending order
    2. dominant label
    3. silhouette measure
    """
    def print_details(self, silhouette):
        ids = []
        for sample in self.samples:
            ids.append(sample.s_id)
        ids.sort()
        cluster_id = ids[0]
        dominant_label = self.dominant_label()
        print(f"Cluster {cluster_id}: {ids}, dominant label = {dominant_label}, silhouette = {silhouette:.3f}")

    """
    for this cluster this function go over all sample and calculate the label with the most occurrences.
    :return the label with the most occurrences.
    """
    def dominant_label(self):
        histogram = {}
        labels = ['B-CELL_ALL', 'B-CELL_ALL_TCF3-PBX1', 'B-CELL_ALL_HYPERDIP', 'B-CELL_ALL_HYPO',
                  'B-CELL_ALL_MLL', 'B-CELL_ALL_T-ALL', 'B-CELL_ALL_ETV6-RUNX1']
        for label in labels:
            histogram[label] = 0
        for sample in self.samples:
            histogram[sample.label] += 1
        max_label_value = -1
        max_label = None
        for label in histogram:
            if max_label_value < histogram[label]:
                max_label = label
                max_label_value = histogram[label]
            elif max_label == histogram[label]:
                max_label = sorted([max_label, label])[0]  # values are the same
        return max_label
