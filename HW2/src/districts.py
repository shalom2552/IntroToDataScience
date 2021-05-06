
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
        districts = []
        for district in self.dataset.get_all_districts():
            if str(district)[0] in letters:
                districts.append(district)
        self.dataset.set_districts_data(districts)

    def print_details(self, features, statistic_functions):
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
                if op == "mean":
                    results.append(s.mean(self.dataset.data[key]))
                if op == "median":
                    results.append(s.median(self.dataset.data[key]))
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
        self.dataset.data['day_type'] = []
        for i in range(len(self.dataset.data['data'])):
            resigned_healed_i = self.dataset.data['resigned_healed'][i]
            new_positive_i = self.dataset.data['new_positives'][i]
            self.dataset.data['day_type'].append(1 if (resigned_healed_i > new_positive_i) else 0)

    def get_districts_class(self):
        """
        making a dictionary with district names as a key
        and 0's or 1's depending on 'green' or 'not-green' as defined.
        :return: dictionary {key: district_name, value: 0,1}
        """
        districts = self.dataset.get_all_districts()
        green_districts = {}
        for district in districts:
            sum_good_days = 0
            for i in range(len(self.dataset.data['data'])):
                if self.dataset.data['denominazione_region'][i] == district and self.dataset.data['day_type'][i] == 1:
                    sum_good_days += 1
            condition = (sum_good_days > 340)
            if condition:
                green_districts[district] = 'green'
            else:
                green_districts[district] = 'not green'
        return green_districts
