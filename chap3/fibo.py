# This calculates the finonacci sequence of a number provided by the user

import math

def main():
	print("This will calculate the Fibonocci sequence for a number you provide")

	n = eval(input("Provide your number: "))

	print("The final product: ", round(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n)/(2 ** n * math.sqrt(5))))

main()