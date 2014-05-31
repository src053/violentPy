#futval.py
# A program to compute the value of an investmen
# carried 10 years into the future

def main():
	print("This program calculates the future value")
	print("of a 10-year investment")

	years = eval(input("Enter the amount of years: "))
	principal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))
	strYears = str(years)
	count = 0

	#print top frame
	print("Year      Value")
	print("---------------")

	for i in range(years):
		principal = principal * (1 + apr)
		print("{0:>3}      ${1:<5.2f}".format(count, principal))
		count = count + 1

	print("The value in {0} years is: ${1:<5.2f}".format(years, principal))

main()