# This program will take the year a user inputs and output the value of easter

def main():
	print("This program will figure out the epact for any given year")

	year = eval(input("Input the year you would like to know the epact of: "))

	#Equation to figure out integer division of C
	C = year//100

	#Equation to figure out epact
	epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

	#Display the epact
	print("The epact is: ", epact)

main()