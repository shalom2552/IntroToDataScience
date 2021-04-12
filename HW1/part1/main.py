import sys
from statistic import sum,mean,median
from data import load_data

# argv[0] - path/main.py
# argv[1] - path/london.csv.py
# argv[2] - arguments
def main(argv):
	question1()
	
	
def question1():
	features=['hum','t1','cnt','season','is_holiday']
	data = load_data("london.csv", features)
	print("Questin 1:")
	print("Summer:")	

	for key in ['hum', 't1', 'cnt']:
		print(data[key])

	print("Holiday:")

	print("All:")


if __name__ == '__main__':
	main(sys.argv)