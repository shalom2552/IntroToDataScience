def sum(values):
	_sum=0
	for value in values:
		_sum += float(value)
	return _sum


def mean(values):
	return sum(values)/len(values)


def median(values):
	length = len(values)
	sort(values) # added 'sort()' in func instead of 'sort()' in calling
	if (length%2)==0:
		return (float(values[(length//2) - 1])+float(values[(length//2)]))/2
	else:
		return values[length//2]

def population_statistics(features_description, data, treatment, target, threshold, is_above, statistic_functions):
		pass
