#Program will calculate a persons pay with wage and hours worked.  after 40 hours its time and a half

def main():

	#prompt user for wage
	wage = eval(input("Please provide employee's hourly wage: "))
	hours = eval(input("Please provide hours worked: "))

	overTime = wage * 1.5

	if hours < 40:
		pay = overTime * hours
		print("Employee's weekly pay is: {0:0.2f}".format(pay))
	else:
		pay = wage * hours
		print("Employee's weekly pay is: {0:0.2f}".format(pay))
main()

