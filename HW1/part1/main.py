import sys
from statistic import sum,mean,median
from data import load_data

# argv[0] - path/main.py
# argv[1] - path/london.csv.py
# argv[2] - arguments
def main(argv):
	features=['hum','t1','cnt','season','is_holiday']
	data = load_data("london_sample.csv", features)
	question1(data)
	
	
def question1(data):
	print("Questin 1:")
	summer_hum=[]
	summer_t1=[]
	summer_cnt=[]
	holiday_hum=[]
	holiday_t1=[]
	holiday_cnt=[]
	all_hum=[]
	all_t1=[]
	all_cnt=[]
	for n in range(len(data[0])):
		if data[3][n] == 1:
			summer_hum.append(data[0][n]) 
			summer_t1.append(data[1][n])
			summer_cnt.append(data[2][n])
		if data[4][n] == 1:
			holiday_hum.append(data[0][n]) 
			holiday_t1.append(data[1][n])
			holiday_cnt.append(data[2][n])
		all_hum.append(data[0][n])
		all_t1.append(data[1][n])
		all_cnt.append(data[2][n])
	
	print("Summer:")	
	print("hum: "+str(sum(summer_hum))+", "+str(mean(summer_hum))+", "+str(median(summer_hum)))
	print("t1: "+str(sum(summer_t1))+", "+str(mean(summer_t1))+", "+str(median(summer_t1)))
	print("cnt: "+str(sum(summer_cnt))+", "+str(mean(summer_cnt))+", "+str(median(summer_cnt)))
	print("Holiday:")
	print("hum: "+str(sum(holiday_hum))+", "+str(mean(holiday_hum))+", "+str(median(holiday_hum)))
	print("t1: "+str(sum(holiday_t1))+", "+str(mean(holiday_t1))+", "+str(median(holiday_t1)))
	print("cnt: "+str(sum(holiday_cnt))+", "+str(mean(holiday_cnt))+", "+str(median(holiday_cnt)))
	print("All:")
	print("hum: "+str(sum(all_hum))+", "+str(mean(all_hum))+", "+str(median(all_hum)))
	print("t1: "+str(sum(all_t1))+", "+str(mean(all_t1))+", "+str(median(all_t1)))
	print("cnt: "+str(sum(all_cnt))+", "+str(mean(all_cnt))+", "+str(median(all_cnt)))


if __name__ == '__main__':
	main(sys.argv)