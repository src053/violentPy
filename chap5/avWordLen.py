#program that will count the number of words in a sentence

def main():

	#get the sentence
	sentence = input("Please input a sentence of any length: ")

	#split the sentence into a list
	split = sentence.split()

	#count the length of the split list
	length = len(split)

	count = 0

	#loop through each word and count the len
	for w in split:
		for i in w:
			count = count + 1

	#calculate average
	av = count / length


	#print the average
	print("The average word length is: {0:0.2f}".format(av))

main()