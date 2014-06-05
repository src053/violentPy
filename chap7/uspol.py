#this program will deccide if you are eligible for us offi9ce

def main():

	#input persons age
	age = eval(input("How old are you: "))

	#input amount of years person has been a citizen
	years = eval(input("How long have you been a US citizen: "))

	if age >= 30 and years >= 9:
		print("You are eliigible to be a US senator and a US represenative")
	else:
		if age >= 25 and years >= 7:
			print("You are eligible to be a US represenative")
		else:
			print("You are not eligible to be a US senator or US represenative, your probably better off")

main()
