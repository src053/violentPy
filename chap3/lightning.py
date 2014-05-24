# This program will calculate the distance a lightning strik was from you
# you will use the delta (in seconds) between seeing the flash and hearing the boom

def main():
	print("This program will calculate the distance (in miles) Lighting was away from you using the time (in seconds) it took from seeing the flash to hearing the boom")

	# prompt user for seconds
	seconds = eval(input("How many seconds was there between seeing the flash and hearing the boom: "))

	# Calculate how many feet away the lighting was
	feet = 1100 * seconds
	# Calculate the miles
	miles = round(feet / 5280, 2)

	# Print how many miles it was out
	print("The lightning was", miles , "miles away")

main()