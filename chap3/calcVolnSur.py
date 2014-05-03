# a program to calculate the volume and surface area of a sphere when provided its radius
import math
def main():
	#print the greeting and what the program does to the user
	print("This application will give us the Volume and Surface of a Sphere when radius is given as input")
	radius = eval(input("What is the radius of the sphere: "))

	volume = 4/3 * (math.pi * (radius ** 3))
	area = 4 * (math.pi * (radius ** 2))

	print("The volume of your sphere is: ", volume)
	print("The area of your sphere is: ", area)
main()
