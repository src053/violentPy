import math

def main():
	print("This program will convert miles to kilometers")
	miles = eval(input("Provide the amount of miles: "))

	kilometers = miles / .62

	print("The amount of kilometers are:", round(kilometers,2))


main()