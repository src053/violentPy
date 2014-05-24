# This program will allow the user to input the amount of numbers they would like to sum
# then prompt for the numbers and sum them

def main():
	print("This program will allow you to vary the amount of numbers you sum")

	amount = eval(input("How many numbers would you like to sum? ")) # The var holding how many times user will be asked to provide numbers
	count = 0 #Initialize the counter var
	total = 0 #Initialize the total var

	#Iterate through all the numbers user said they would like to add
	while(count < amount):
		num = eval(input("What number would you like to add to the sum? "))
		total = total + num
		count += 1
	print("The total is: ", total)

main()