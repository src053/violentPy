# Program to find the averge of numbers in a file

def main():
	#Get the filename with the numbers
	fileName = input("What file are the numbers in? ")
	#var to contain all the content of the file
	infile = open(fileName, 'r')
	#var to keep track of the sum of those numbers
	sum = 0.0
	#var to keep track of the sum
	count = 0
	#var with the first line of the file
	line = infile.readline()
	#iterate through all lines in the document
	while line != "":
		#math to sum the line with the total sum
		print(line)
		sum = sum + eval(line)
		print(sum)
		#increment the count var by 1
		count = count + 1
		#read in the next line of the file
		line = infile.readline()
	print("\nThe average of the numbers is", sum / count)

main()