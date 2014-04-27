#futval.py
# A program to compute the value of an investmen
# carried 10 years into the future

def main():
	print("This program calculates the future value")
	print("of a 10-year investment")

	years = eval(input("Enter the amount of years: "))
	strprincipal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))
	strYears = str(years)
	principal = strprincipal


	for i in range(years):
		print(principal)
		principal = principal * (1 + apr)
		principal += strprincipal

	print("The value in " + strYears + " years is: ", principal)

main()