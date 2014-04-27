# this is a interactive calulator
import math

def main():
	print("This program will let you evalute 100 equations")

	i=1
	while(i<100):
		solution = eval(input("Enter an equation you would like solved: "))

		print("solution is:", round(solution, 2))

main()