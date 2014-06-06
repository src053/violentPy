#program will copute the year of easter between 1982 and 2048

def calcabc(year):
	a = year%19
	b = year%4
	c = year%7
	return a,b,c

def calcd(a):
	return (19 * a + 24)%30

def calce(a,b,c,d):
	return (2 * b + 4 * c + 6 * d + 5)%7

def calcEaster(d,e):
	return (22 + d + e)

def calcMonth(easter):
	if easter > 31:
		return 4
	else:
		return 3


def main ():
	#get the year
	year = eval(input("Please input the year you are interested in finding out easter: "))

	#calculations for a,b,c
	a, b, c = calcabc(year)

	#calculations for d
	d = calcd(a)

	#calculations for e
	e = calce(a,b,c,d)

	#calculate easter
	easter = calcEaster(d,e)

	#find out if easter is in march or april
	month = calcMonth(easter)

	#give the date of easter
	if month == 3:
		print("Easter is on March {0} in {1}".format(easter, year))
	else:
		easterApril = easter - 31
		print("Easter is on April {0} in {1}".format(easterApril, year))

main()




