import sys

def main(argv):
	print("Hello world")
	list = [1,2,3,5]
	print(med(list))
	print(sum(list))
	print(average(list))


def sum(list):
	sum=0
	for element in list:
		sum += float(element)
	return sum


def average(list):
	return sum(list)/len(list)


def med(list):
	length = len(list)
	if (length%2)==0:
		return (float(list[length//2 - 1])+float(list[(length//2)]))/2
	else:
		return list[length/2]


if __name__ == '__main__':
	main(sys.argv)