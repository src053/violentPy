#program to determing speeding fine

def main():

	#get the speed limit
	speedLimit = eval(input("Please enter the speed limit: "))
	#get the speed the person was traveling
	mph = eval(input("Please enter how fast the vehicle was going: "))
	#setfine to zero
	fine = 0

	if mph > speedLimit:
		over = mph - speedLimit
		for i in range(over):
			fine = fine + 5
		if mph > 90:
			fine = fine + 200
		print("Driver was over the speed limit {0}mph and will be fined ${1:0.2f} dollars".format(over, fine))
	else:
		print("Driver was within speed limit, thanks for being polite")

main()