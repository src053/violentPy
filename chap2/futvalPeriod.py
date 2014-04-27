#futval.py
# A program to compute the value of an investmen
# carried 10 years into the future
import math
def main():
	print("This program calculates the future value")
	print("of a 10-year investment")

	years = eval(input("Enter the amount of years: ")) # need the years you will keep the investment
	strPrincipal = eval(input("Enter the initial principal: ")) # need the starting amount of $$$
	periods = eval(input("Enter the number of compounding periods: ")) # how many compounding periods per year
	apr = eval(input("Enter the annual interest rate: ")) # the interest rate to be earned
	#strYears = str(years)
	principal = strPrincipal #this var will be used as the principal in the loop, we need strPrincipal to 
	periodPercent = apr / periods #this var will be the rate percentage used in the loop
	numberLoops = years * periods #This var is the amount of loops



	for i in range(numberLoops):
		print(round(principal))
		principal = principal * (1 + periodPercent)
		#principal += strPrincipal

	print("The value in ", years, " years is: ", round(principal, 2))
main()