import pandas


def load_data(path, features):
	"""
	param path: full path to the file
	param features: list of relevant features we interest on
	this func read the relevant features and loaded it to the main memory
	returens the data with relevant colomns
	"""
	data_new=[]
	df = pandas.read_csv(path)
	data = df.to_dict(orient="list")
	for colomn in features:
		data_new.append(df[colomn])
	return data_new

def filter_by_feature(data, features, values):
	"""
	param data: dictionary keys from data set and values of them
	param features: name of categorical programs
	param values: set of values so that features can get all of the values in 'values'
	this func read the relevant features and loaded it to the main memory
	return‬‬ ‫‪data1,‬‬ ‫‪data2‬‬: returens tow dictioneris so that trheir union will make the all data 
	and data1 will have all rows so that fetures got some equal value in values, and so for data2
	"""
	pass

def print_details(data, features, statistic_functions):
	"""
	param data: dictionary keys from data set and values of them
	param features: list of features from the data set
	srtatistic_functions: list of statistic function from 'statistic.py'
	"""
	pass
