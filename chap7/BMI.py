#program to determine body mass index

def main():

	#get personal info
	height = eval(input("Please provide your height in inches: "))
	weight = eval(input("Please provide your weight in pounds: "))

	bmi = (weight * 720)/(height ** 2)

	if bmi <= 25 and bmi >= 16:
		print("Your BMI of, {0:0.02f} is healthy".format(bmi))
	else:
		print("Your BMI of, {0:0.02f} is un-healthy".format(bmi))

main()