
def sum(values):
	_sum = 0
	for value in values:
		_sum += float(value)
	return _sum


def mean(values):
	return sum(values)/len(values)


def median(values):
	values = sorted(values)
	length = len(values)
	if (length % 2) == 0:
		return (float(values[(length//2) - 1])+float(values[(length//2)]))/2
	else:
		return float(values[length//2])


def population_statistics(features_description, data, treatment, target, threshold, is_above, statistic_functions):
	from data import print_details  # non in-function import will cause circular import
	print(features_description)
	print_details(data, target, statistic_functions)
