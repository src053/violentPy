# this program will take the input of three sides of a triangle and calculate the area

import math
def main():
	print("This program will calculate the Area of a triangle when the length of three sides are provided")
	a = eval(input("Length of side a: "))
	b = eval(input("Length of side b: "))
	c = eval(input("Length of side c: "))

	s = (a + b + c) / 2
	area = round(math.pi * (s * ((s - a)*(s - b)*(s - c))), 2)

	print("The area of the triangle is: ", area)

main()