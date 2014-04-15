#A simple program illustration chaotic behavior.
#Example from Python programing

def main(): # define the function main
	print ("this program illustrates a caotic function") #print somethign to the user
	x = eval(input("Enter a number between 0 and 1: ")) #print question to user then assign the input to x var
	for i in range(10): # loop 10 times with the for loop
		x = 2.0 * x * (1 - x) #re-define the x var with new assignment
		print (x) #print the value of x to user

main() #call main function