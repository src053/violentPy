#program to accept exam score and print grade

def main():

	#Get score of test
	score = eval(input("Input score: "))

	if score > 89:
		grade = "A"
	elif score > 79:
		grade = "B"
	elif score > 69:
		grade = "C"
	elif score > 59:
		grade = "D"
	else:
		grade = "F"

	print("Congrats you got a: ", grade)

main()