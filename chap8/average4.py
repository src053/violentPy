#program to average many numbers

def main():
	#var for sum of all numbers
	sum = 0.0
	#var for how many loops one takes
	count = 0
	#var for value of number
	xStr = input("Enter a number (<Enter> to quit) >> ")

	#create loop while there is a value in xStr
	while xStr != "":
		x = eval(xStr)
		sum = sum + x
		count = count + 1
		xStr = input("Enter a number (<Enter> to quit) >> ")
	print("\nThe average of the numbers is", sum/count)

main()
