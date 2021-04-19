import pandas as pd
from statistic import sum,mean,median


def load_data(path, features):
	"""
	@param path: full path to the file
	@param features: list of relevant features we interest on
	this func read the relevant features and loaded it to the main memory
	@return data: the data with relevant columns
	"""
	df = pd.read_csv(path, usecols=features)
	data = df.to_dict(orient="list")
	return data


def filter_by_feature(data, feature, values):
	"""
	@param data: dictionary keys from data set and values of them
	@param feature: name of categorical programs
	@param values: set of values so that features can get all the values in 'values'
	this func read the relevant features and loaded it to the main memory
	@return data1,data2: returns tow dictionaries so that their union will make the all data
	and data1 will have all rows so that features got some equal value in values, and so for data2
	"""
	dict1={}
	dict2={}
	length = len(data[feature])
	for key in data:
		dict1[key] =[]
		dict2[key]=[]
	for n in range(length):
		if data[feature][n] in values:
			for key in data:
				dict1[key].append(data[key][n])
		else:
			for key in data:
				dict2[key].append(data[key][n])
	return dict1, dict2


def print_details(data, features, statistic_functions):
	"""
	@param data: dictionary keys from data set and values of them
	@param features: list of features from the data set
	@param statistic_functions: list of statistic function from 'statistic.py'
	"""
	for key in features:
		results = []
		print(key+": ", end='')
		for op in statistic_functions:
			if op == "sum":
				results.append(sum(data[key]))
			if op == "mean":
				results.append(mean(data[key]))
			if op == "median":
				results.append(median(data[key]))
		length = len(results)
		for n in range(length):
			print(results[n], end='')
			if n != length-1:
				print(", ", end='')
		print("")

