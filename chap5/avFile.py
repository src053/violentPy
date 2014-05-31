#program that will count the number of words in a sentence from within a file

def main():

	#get the name of file
	fname = input("Please enter the name of the file: ")
	#open the file
	infile = open(fname, "r")

	#read in file
	read = infile.read()

	#split the sentence into a list
	split = read.split()

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