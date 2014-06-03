#Program to determine exam scores using if 

def main():

	#input scores
	score = eval(input("Please provid the exam score (0 thru 100): "))

	if score >= 90 and score <=100:
		print("Congradulations you studied hard and got a A!")
	elif score >= 80:
		print("Congradulations you studied hard and got a B!")
	elif score >= 70:
		print("Not bad you passed with a C")
	elif score >= 60:
		print("Better work a bit harder you got a D")
	else:
		print("Sorry to say you failed the test with a F")

main()