import sys
from statistic import sum,mean,median
from data import load_data, filter_by_feature

# argv[0] - path/main.py
# argv[1] - path/london.csv.py
# argv[2] - arguments
def main(argv):
	features=['hum','t1','cnt','season','is_holiday']
	data = load_data("london_sample.csv", features) # sample only!
	question1(data)
	features=['t1','cnt','season','is_holiday']
	data = load_data("london_sample.csv", features) # sample only!
	question2(data)	


def question1(data):
	print("Questin 1:")
	print("Summer:")
	dict1,dict2=filter_by_feature(data, 'season', [1])
	for key in ['hum', 't1', 'cnt']:
		print(key,": "+str(sum(dict1[key]))+", "+str(mean(dict1[key]))+", "+str(median(sorted(dict1[key]))))
	print("Holiday:")
	dict1,dict2=filter_by_feature(data, 'is_holiday', [1])
	for key in ['hum', 't1', 'cnt']:
		print(key,": "+str(sum(dict1[key]))+", "+str(mean(dict1[key]))+", "+str(median(sorted(dict1[key]))))
	print("All:")
	dict1 = data
	for key in ['hum', 't1', 'cnt']:
		print(key,": "+str(sum(dict1[key]))+", "+str(mean(dict1[key]))+", "+str(median(sorted(dict1[key]))))
	

def question2(data):
	# season split
	winter, non_winter = filter_by_feature(data, 'season',[3])
	Holiday, weekday = filter_by_feature(winter, 'is_holiday', [1])
	holyday_bigger, holyday_smaller = split_by_value(Holiday,13)
	weekday_bigger, weekday_smaller = split_by_value(weekday,13)

	print("Questin 2:")
	#for dict in [holyday_smaller, weekday_smaller, holyday_bigger, weekday_bigger]:
	print("cnt:"+str(mean(holyday_bigger['cnt']))+", "+str(median(sorted(holyday_bigger['cnt']))))




def split_by_value(data, value):
	dict1={}
	dict2={}
	length = len(data['t1'])
	for key in data:
		dict1[key] =[]
		dict2[key]=[]
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