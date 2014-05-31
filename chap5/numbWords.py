#program that will count the number of words in a sentence

def main():

	#get the sentence
	sentence = input("Please input a sentence of any length: ")

	#split the sentence into a list
	split = sentence.split()

	#count the length of the split list
	length = len(split)

	#print the length
	print("The length of the sentence is: ", length)

main()