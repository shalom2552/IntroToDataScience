import pandas as pd


class Data:
    # path - full path to the dataset
    def __init__(self, path):
        df = pd.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """
        gets all the districts names in the dataset ( denominazione_region )
        :return: list of all districts names in the dataset
        """
        region_names = []
        for region_name in self.data['denominazione_region']:
            if region_name not in region_names:
                region_names.append(region_name)
        return region_names

    def set_districts_data(self, districts):
        """
        get all the records which their district names is in the following district list
        :param districts: list districts names
        :return: dataset only of the districts giving
        """
        data = self.data
        new_dict = {}
        for key, value in data.items():
            new_dict[key] = []
        for i in range(len(data['data'])):
            if data['denominazione_region'][i] in districts:
                for key in data:
                    new_dict[key].append(data[key][i])
        self.data = new_dict
