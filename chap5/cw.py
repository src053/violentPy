#program that will count the number of words in a sentence from within a file

def main():

	#get the name of file
	fname = input("Please enter the name of the file: ")
	#open the file
	infile = open(fname, "r")

	#read in file
	allLines = infile.readlines()

	#count the number ofsentence in a list
	lines = len(allLines)

	#var to count letters
	letters = 0

	#var to count words
	words = 0

	#loop through each line and enumerate the amount of words and letters
	for w in allLines:
		#remove the trailing \n
		swap1 = w[:-1]
		#test the value of swap 1
		print(swap1)

		#split the line into list of words
		spl = swap1.split()

		#test the value of spl
		print(spl)

		words = words + len(spl)
		
		#loop through each word and count the letters
		for l in swap1:
			print(l)
			letters = letters + 1


	#print the totals
	print("The total number of lines is: {0}".format(lines))
	print("The total number of words is: {0}".format(words))
	print("The total number of letters is: {0}".format(letters))

main()