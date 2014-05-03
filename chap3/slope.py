# This program will calculate the slope of to points on a graph
# User will be required to input for var's x1, x2, y1, y2
import math

def slope(x1, x2, y1, y2):
	return round((y2 - y1)/(x2 - x1)) #Calculate and return the slope

def distance(x1, x2, y1, y2):
	return round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)

def main():
	print("This program takes to points on a graph and finds the slope")
	print()

	x1 = eval(input("Enter the x1 location: ")) #prompt for x1 location
	y1 = eval(input("Enter the y1 location: ")) #prompt for y1 location
	x2 = eval(input("Enter the x2 location: ")) #prompt for x2 location
	y2 = eval(input("Enter the y2 location: ")) #prompt for y2 location
	choice = eval(input("If you want the slope type 1 type anything else for the distance: ")) #prompt user for what equation they want done

	if choice == 1:
		s = slope(x1, x2, y1, y2)
		print("The slope is: ", s)
	else:
		d = distance(x1, x2, y1, y2)
		print("The distance is: ", d)


main()