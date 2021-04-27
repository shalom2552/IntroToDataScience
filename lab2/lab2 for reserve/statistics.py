from math import sqrt  # TODO import is permitted?


def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)  # round to int required because division always produces float
    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values) / len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average) ** 2 for x in list_of_values])
    return squared_sum / (len(list_of_values) - 1)


def covariance(first_list_of_values, second_list_of_values):
    """
    calculating the covariance of a two list (x, y) by the formula : [(x[i]-x_mean)*(y[i]-y_mean)]/(n-1)
    :param first_list_of_values:
    :param second_list_of_values:
    :return: the covariance of the two lists
    """
    result, sigma = 0, 0
    # get the data as x, y, n
    n = len(first_list_of_values)
    x, y = first_list_of_values, second_list_of_values
    x_mean, y_mean = sum(first_list_of_values) / n, sum(second_list_of_values) / n
    # sigma (x[i]-x_mean)*(y[i]-y_mean) and then dividing by (n-1)
    for i in range(n):
        sigma += (x[i] - x_mean) * (y[i] - y_mean)
    result = sigma / (n - 1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    calculating the correlation of a two list (x, y) by the formula : cov(x,y)/(std_y * std_x)
    :param first_list_of_values:
    :param second_list_of_values:
    :return: the correlation of the two lists
    """
    std_x = sqrt(variance(first_list_of_values))  # TODO import is permitted?
    std_y = sqrt(variance(second_list_of_values))  # TODO import is permitted?
    cov_xy = covariance(first_list_of_values, second_list_of_values)
    result = cov_xy / (std_y * std_x)
    return result
