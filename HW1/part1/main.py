import sys
from statistic import sum,mean,median
from data import load_data,  filter_by_feature

# argv[0] - path/main.py
# argv[1] - path/london.csv.py
# argv[2] - arguments
def main(argv):
	features=['hum','t1','cnt','season','is_holiday']
	data = load_data("london_sample.csv", features) # sample only!
	question1(data)
	
	
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
	

if __name__ == '__main__':
	main(sys.argv)