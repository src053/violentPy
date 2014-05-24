#this program will find the sum of natural numbers when user provides n

import math

def main():
	#Describes the program
	print("This program will sum the natural numbers in 'n'") 

	n = eval(input("Input your number: ")) #var for n
	total = 0 #initializes the total va
	count = 1 #initializes the counter

	#Iterates until you have reached n
	while(count <= n):
		total = total + count #adds the count to total
		print(total) #prints total 
		count += 1 #iterates the count by one

	#displays the value of total
	print("The total is: ", total)

main()