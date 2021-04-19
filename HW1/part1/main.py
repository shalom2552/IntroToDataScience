import sys
from statistic import sum,mean, median, population_statistics
from data import load_data, filter_by_feature, print_details


# argv[0] - path/main.py
# argv[1] - path/london.csv.py
# argv[2] - arguments
def main(argv):
	features = ['hum', 't1', 'cnt', 'season', 'is_holiday']
	data = load_data("london.csv", features)
	question1(data)
	features = ['t1', 'cnt', 'season', 'is_holiday']
	data = load_data("london.csv", features)
	print("")
	question2(data)	


def question1(data):
	print("Question 1:")
	print("Summer:")
	winter, non_winter=filter_by_feature(data, 'season', [1])
	features = ['hum', 't1', 'cnt']
	statistic_functions = ['sum', 'mean', 'median']
	print_details(winter, features, statistic_functions)
	print("Holiday:")
	holiday, non_holiday=filter_by_feature(data, 'is_holiday', [1])
	print_details(holiday, features, statistic_functions)
	print("All:")
	print_details(data, features, statistic_functions)


def question2(data):
	# season split
	print("Question 2:")
	winter, non_winter = filter_by_feature(data, 'season',[3])
	holiday, weekday = filter_by_feature(winter, 'is_holiday', [1])
	holiday_smaller, holiday_bigger = split_by_value(holiday,13)
	weekday_smaller, weekday_bigger = split_by_value(weekday,13)
	functions = ['mean','median']
	print("If t1<=13.0, then:")
	population_statistics("Winter holiday records:",holiday_smaller,'t1',['cnt'],13,False,functions)
	population_statistics("Winter weekday records:",weekday_smaller,'t1',['cnt'],13,False,functions)
	print("If t1>13.0, then:")
	description = "Winter holiday records:" 
	population_statistics("Winter holiday records:",holiday_bigger,'t1',['cnt'],13,False,functions)
	population_statistics("Winter weekday records:",weekday_bigger,'t1',['cnt'],13,False,functions)


def split_by_value(data, value):
	dict1 = {}
	dict2 = {}
	length = len(data['t1'])
	for key in data:
		dict1[key] = []
		dict2[key] = []
	for n in range(length):
		if data['t1'][n] <= value:
			for key in data:
				dict1[key].append(data[key][n])
		else:
			for key in data:
				dict2[key].append(data[key][n])
	return dict1, dict2


if __name__ == '__main__':
	main(sys.argv)
