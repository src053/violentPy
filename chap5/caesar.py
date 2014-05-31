#program to use ceasar cipher

def main():

	#Input phrase and key
	encrypt = input("Please provide one word to encrypt: ")
	key = eval(input("Please input a numeric key: "))

	#var for storing encrypted message
	message = ""

	#loop through each letter and make a change
	for i in encrypt:
		message = message + (chr(ord(i) + key))

	#print the encrpted word
	print(message)
main()
