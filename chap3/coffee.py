# THis program will calculate the cost of shipping per order of coffee

def main():

	print("This program will calculate the cost of shipping coffee")

	
	coffee = 10.50 #cost of coffee var
	weight = eval(input("How many pounds of coffe are in the order: ")) #the weight of the order var
	total = (weight * .86) + (coffee * weight) + 1.50 #the calculation of the total cose

	#display the total cost to the user
	print("The total cost of the shipment will be: ", round(total, 2))

main()