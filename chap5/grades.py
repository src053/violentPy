# Program accepts a quiz score and prints out a grade

def main():

	#Create list
	letter = ["F", "F", "D", "C", "B", "A"]
	#prompt for quiz score
	score = eval(input("Input score: "))

	#set grade
	grade = letter[score]

	#print grade
	print("Congrats you got a: ", grade)

main()

