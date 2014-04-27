def main():
	print("This program will convert farenheit to celcius")
	farenheit = input(eval("Provide the farenheit value: "))

	celcius = (farenheit - 32) * 5/9

	print("The temperatur in Celius is", celcius)


main()