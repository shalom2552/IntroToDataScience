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
        pass

    def set_districts_data(self,districts):
        """
        get all the records which their district names is in the following district list
        :param districts: list districts names
        :return: dataset only of the districts giving
        """
        pass
