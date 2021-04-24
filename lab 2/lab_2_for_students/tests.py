import statistics as s
import numpy as np
import random as r
import sys


class bcolor:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	ENDC = '\033[0m'


def main(argv):
	n = int(argv[1])
	x = []
	y = []
	for _ in range(n):
		x_i=[]
		y_i=[]
		for  i in range(n):
			x_i.append(r.uniform(-500,500))
			y_i.append(r.uniform(-500,500))
		x.append(x_i)
		y.append(y_i)
	
	print(bcolor.WARNING+">>>>>>>>>>>>>>  covariance  <<<<<<<<<<<<<<<"+ bcolor.ENDC)
	cov(x, y, n)
	print(bcolor.WARNING+">>>>>>>>>>>>>  correlation  <<<<<<<<<<<<<<<"+bcolor.ENDC)
	corr(x,y,n)
	

def cov(x, y, n):
	for  i in range(n):
		covnp = np.cov(x[i],y[i])
		covs = s.covariance(x[i],y[i])
		if(int(covnp[1][0])==int(covs)):
			printpass()
		else:
			printfail()
		printYE(covs, covnp[1][0])


def corr(x, y, n):
	for  i in range(n):
		corrnp = np.corrcoef(x[i],y[i])
		corrs = s.correlation(x[i],y[i])
		if(int(corrnp[1][0])==int(corrs)):
			printpass()
		else:
			printfail()
		printYE(corrs, corrnp[1][0])


def printfail():
	print(bcolor.WARNING + "\tFAIL!" + bcolor.ENDC)


def printpass():
	print(bcolor.OKGREEN + "\tPASS!" + bcolor.ENDC)


def printYE(your, expected):
	print("*\tYour:\t\t",your)
	print("*\tPASSExpected:\t",expected)
	print("************************************************")


if __name__ == '__main__':
	main(sys.argv)

