#A program to convert Celsius temps to Fahrenheit

def main():
	print("This program will convert celsius to farenheit")
	count = 0
	celsius = 0
	
	while(count < 10):
		fahrenheit = 9/5 * celsius + 32
		print("The temperature is", fahrenheit, "degree Fahrenheit.")
		count += 1
		celsius = celsius + 10

main()