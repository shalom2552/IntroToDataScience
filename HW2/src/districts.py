class Districts:
    # constructor
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_district(self, letters):
        """
        update the dataset with the district that their names starting with one of the letters set
        :param letters: set of letters
        :return: the dataset after filtering
        """
        pass  # TODO implement

    def print_details(self, data, features, statistic_functions):
        """
        :param data: dictionary keys from data set and values of them
        :param features: list of features from the data set
        :param statistic_functions: list of statistic function from 'statistic.py'
        """
        import statistics as s
        for key in features:
            results = []
            print(key + ": ", end='')
            for op in statistic_functions:
                if op == "sum":
                    results.append(sum(data[key]))  # TODO need this?
                if op == "mean":
                    results.append(s.mean(data[key]))
                if op == "median":
                    results.append(s.median(data[key]))
            length = len(results)
            for n in range(length):
                print(results[n], end='')
                if n != length - 1:
                    print(", ", end='')
            print("")

    def determine_day_type(self):
        """
        add key column to the Dataset named "day_type", with value 0,1
        1 means good-day
        0 means bad-day
        based on statistics
        :return: the Dataset  # TODO is needed?
        """
        pass

    def get_districts_class(self):
        """
        making a dictionary with district names as a key
        and 0's or 1's depending on 'green' or 'not-green' as defined.
        :return: dictionary {key: district_name, value: 0,1}
        """
        pass
