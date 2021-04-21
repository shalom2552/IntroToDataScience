from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:.2f}, Std: {:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values) ** 0.5))

    # computing correlations, pair should be sorted before printing.
    # choose to list for each iteration
    correlations = calculate_correlation_of_all_lists(data)
    max_correlation = max_pair(correlations)
    min_correlation = min_pair(correlations)
    print(max_correlation)
    strongest_pair = max_correlation[0]
    high_correlation = max_correlation[1]
    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    weakest_pair = min_correlation[0]
    low_correlation = min_correlation[1]
    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


def calculate_correlation_of_all_lists(data):
    """
    calculate the correlation for each to pairs of headers from data
    :param data: dictionary of headers and list values
    :return: returns list of all the pairs and their correlations
    """
    data_header, data_values, correlations = [], [], []
    for feature_name, list_of_values in sorted(data.items()):
        data_header.append(feature_name)
        data_values.append(list_of_values)
    for i in range(len(data_header)):
        for j in range(len(data_header)):
            if i == j:
                continue
            current_correlation = correlation(data_values[i], data_values[j])
            pair = [data_header[i], data_header[j]]
            correlations.append([sorted(pair), current_correlation])
    return correlations


def max_pair(nested_list):
    """
    calculate the pair with the max value
    :param nested_list: list of list of pairs and values
    :return: returns the pair with the max value: [["header1", "header2"], correlation_value]
    """
    maximum = nested_list[0]  # nested_list[0]: [["header1", "header2"], correlation_value]
    for elem in nested_list:
        if elem[1] > maximum[1]:
            maximum = elem
    return maximum


def min_pair(nested_list):
    """
    calculate the pair with the min absolute value
    :param nested_list: list of list of pairs and values
    :return: returns the pair with the min absolute value: [["header1", "header2"], correlation_value]
    """
    minimum = nested_list[0]
    for elem in nested_list:
        if abs(elem[1]) < abs(minimum[1]):
            minimum = elem
    return minimum


if __name__ == '__main__':
    run_analysis()
