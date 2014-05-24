# This program will determine the length of the ladder required to 
# reach a height on a house when you have that height and the angle of the ladder

import math
def main():
	# Program description
	print("This program will find the height a ladder will need to be when given two inputs")
	print("1) The height of the house 2) the angle (in degrees) of the ladder")

	height = eval(input("Please provide the height of the house: ")) # The var that contains the height of the house
	degrees = eval(input("Please provide the angle of the ladder against the house: ")) # The var that contains the degree angle of the ladder

	radians = (math.pi / 180) * degrees # The equation to find the radian
	length = round(height / math.sin(radians), 2) # The equation to find the needed length of the ladder

	# Print the length of the ladder
	print("length the ladder will need to be: ", length)

main()