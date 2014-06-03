#Program to determine what year class you are in

def year(credits):

	#determin what grade student is in
	if credits < 7:
		print("Student is a Freshman")
	elif credits > 7 and credits < 16:
		print("Student is a Sophmore")
	elif credits > 16 and credits < 26:
		print("Student is a senior")
	else:
		print("did you put in a number 1-26?")
		
def main():

	#get the number of credits a student has
	credits = eval(input("Please provide the amount of credits student has: "))

	year(credits)

main()