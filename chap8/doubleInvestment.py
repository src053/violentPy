#Program that takes the starting interest rate and tells you how long it will take to double

#function for the calculation of interest
def calculation(interest, investment):
	#return the new value of investment var
	return investment * (1 + interest)

def main():

	#var that will contain the interest rate
	interest = eval(input("Please provide the interest rate: "))

	#var for principal investment
	principal = 1
	#var to count the years
	years = 0
	#var for investment
	investment = principal

	#while iteration until investment var doubles
	while investment <= principal * 2:
		#use the calculation function to calculate ivestment value
		investment = calculation(interest, investment)
		#debug line
		print("{0:0.2f}".format(investment))
		#increment the years var by one
		years = years + 1

	#print the years it took to double
	print("It took {0} years to double the investment".format(years))

main()