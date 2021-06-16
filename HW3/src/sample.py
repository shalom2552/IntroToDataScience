

class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.label = label
        self.genes = genes

    def compute_euclidean_distance(self, other):
        sum_sqr_dis = 0
        for i in range(len(self.genes)):
            sum_sqr_dis += (self.genes[i] - other.genes[i])**2
        return sum_sqr_dis**(1/2)
