# A program to calculate cost per square inch of pizza
# You will need to input values 1) diameter of the pizza 2)cost of the pizza

import math

def main():
	print("This program will calculat the cost per square inch of Pizza")
	diameter = eval(input("what is the radius of the pizza: "))
	tCost = eval(input("What is the cost of the pizza: "))

	radius = diameter * .5
	area = math.pi * (radius ** 2)
	sqInCost = tCost / area

	print("The cost per square inch is", round(sqInCost, 4))


main()