#program to calculate how much the baby sitter should be paid


def overtime(start, end):

	#calculate regular hours
	regularHours = 9.5 - start
	#calculate overtime hours
	overtimeHours = end - 9.5

	#calculate regular pay
	regularPay = regularHours * 2.5
	#calculate overtime pay
	overtimePay = overtimeHours * 1.75

	#caculate total pay
	totalPay = regularPay + overtimePay

	print("The total pay for sitter is ${0:0.2f} dollars".format(totalPay))

def standardTime

def main():

	#get the start time of sitter
	start = eval(input("Please provide the start time in half hour increments (example 6.5 for 6:30): "))

	#get the end time
	end = eval(input("Please provide the end time in half hour increments (example 9.5 for 9:30): "))

	hours = end - start

	if end > 9.5:
		overtime(start, end)
	else:
		standardtime(start, end)




