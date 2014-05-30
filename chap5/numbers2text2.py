#A program to convert a sequence of Unicode numbers into a string of text.
# Efficient version using a list accumulator.

def main():
	print("This program converts a sequence of Unicode numbers into")
	print("the string of tect that it represents.\n")

	#get the message encode
	inString = input("Please enter the Unicode-encoded message: ")

	#Loop through each substring and build Unicode message
	chars = []
	for numStr in inString.split():
		codeNum = eval(numStr)
		chars.append(chr(codeNum))

	message = "".join(chars)
	print("\nThe decoded message is:", message)

main()