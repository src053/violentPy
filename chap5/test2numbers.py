# A program to convert a textual messafe into a sequnce of
#	numbers, utilizing the underlying Unicode encoding.

def main():
	print("This program converts a textual messafe into a sequenc")
	print("of numbers representing the Unicode encoding of the message. \n")

	#get the message to encode
	message = input("Please enter the message to encode: ")

	print("\nHere are the Unicode codes:")

	#Loop through the message and print out the Unidcode values
	for ch in message:
		print(ord(ch), end=" ")

	print() #blank line prior to prompt

main()