# This program will calculate the distance a lightning strik was from you
# you will use the delta (in seconds) between seeing the flash and hearing the boom

def main():
	print("This program will calculate the distance (in miles) Lighting was away from you using the time (in seconds) it took from seeing the flash to hearing the boom")

	seconds = eval(input("How many seconds was there between seeing the flash and hearing the boom: "))

	feet = 1100 * seconds
	miles = round(feet / 5280, 2)

	print("The lightning was", miles , "miles away")

main()