import numpy as np


class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        sum_sqr_dis = 0
        for i in range(len(self.label)):
            sum_sqr_dis += (self.label[i] - other.label[i])**2
        return np.sqrt(sum_sqr_dis)
