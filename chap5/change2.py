# A program to calvulate the value of some change in dollars
# This version represents the total cash in cents.

def main():
	print("Change Counter\n")

	print("Please enter the count of each coin typr.")
	quarters = eval(input("Quarters: "))
	dimes = eval(input("Dimes: "))
	nickels = eval(input("Nickels: "))
	pennies = eval(input("Pennies: "))

	total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

	print("THe total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

main()