import pandas as pd
from sample import Sample


class Data:
    # path - full path to the dataset
    def __init__(self, path):
        df = pd.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        samples = []

        samples_id = self.data['samples']
        samples_type = self.data['type']
        samples_genes = []
        for element in self.data:
            if element != 'samples' and element != 'type':
                samples_genes.append(self.data[element])

        for i in range(len(samples_id)):
            genes = []
            for j in range(len(samples_genes)):
                genes.append(samples_genes[j][i])
            sample = Sample(samples_id[i], genes, samples_type[i])
            samples.append(sample)
        return samples
