#A simple program illustration chaotic behavior.
#Example from Python programing

def main(): # define the function main
	print ("this program illustrates a caotic function") #print somethign to the user
	x = eval(input("Enter a number between 0 and 1: ")) #print question to user then assign the input to x var
	n = eval(input("How many numbers should I print? "))
	for i in range(n): # loop 10 times with the for loop
		x = 3.9 * x * (1 - x) #re-define the x var with new assignment
		print (x) #print the value of x to user

main() #call main function