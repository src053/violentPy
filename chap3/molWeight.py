# This program will calculate the weight of thre different atoms Hydrogen, Carbon, and Oxygen
# You will input the number of atoms per molecule

def main():
	h = 1.0079 #hydrogen weight
	c = 12.011 # carbon weight
	o = 15.9994 #Oxygen weight

	# Prompts for the number of molecules per element
	noH = eval(input("Enter the number of Hydrogen molecules: "))
	noC = eval(input("Enter the number of Carbon molecules: "))
	noO = eval(input("Enter the number of Oxygen molecules: "))

	#Calculate the total weight of each element
	totalH = h * noH
	totalC = c * noC
	totalO = o * noO

	# Display the weight of each element
	print("The total weight of Hydrogen is: ", round(totalH, 5))
	print("The total weight of Carbon is: ", round(totalC, 5))
	print("The total weight of Oxygen is: ", round(totalO, 5))
	# Display the weight of all elements
	print("The total of all molecules is: ", round(totalO + totalC + totalH, 4))

main()