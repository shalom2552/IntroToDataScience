def mean(values):
	_sum = 0
	for value in values:
		_sum += float(value)
	return _sum/len(values)


def median(values):
	values = sorted(values)
	length = len(values)
	if (length % 2) == 0:
		return (float(values[(length//2) - 1])+float(values[(length//2)]))/2
	else:
		return values[length//2]
