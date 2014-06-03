#Program to determine exam scores using if 

def main():

	#input scores
	score = eval(input("Please provid the exam score (0 thru 5): "))

	if score == 5:
		print("Congradulations you studied hard and got a A!")
	elif score == 4:
		print("Congradulations you studied hard and got a B!")
	elif score == 3:
		print("Not bad you passed with a C")
	elif score == 2:
		print("Better work a bit harder you got a D")
	else:
		print("Sorry to say you failed the test with a F")

main()