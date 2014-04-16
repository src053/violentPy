#A simple program illustration chaotic behavior.
#Example from Python programing

def main(): # define the function main
	print ("this program illustrates a caotic function") #print somethign to the user
	x = eval(input("Enter a number between 0 and 1: ")) #print question to user then assign the input to x var
	n = eval(input("How many numbers should I print? "))
	num = eval(input("Which algebraic formula would you like to use? Choose 1, 2, or 3: "))

	if num == 1:
		exp1(x, n)
	elif num == 2:
		exp2(x, n)
	else:
		exp3(x, n)
	
def exp1(x, n): #first algebric expression
	print("We will use formula 3.9 * x * (1 - x)")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * x * (1 - x) #re-define the x var with new assignment
		print (x) #print the value of x to user
		li = li + x
	return li

def exp2(x, n): #second algebric expression
	print("We will use formula 3.9 * (x - x * x)")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * (x - x * x) #re-define the x var with new assignment
		print (x) #print the value of x to user
		li = li + x
	return li

def exp3(x, n): #Third algebric expression
	print("We will use formula 3.9 * x - 3.9 * x * x")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * x - 3.9 * x * x #re-define the x var with new assignment
		print (x) #print the value of x to user
	return li

def displayTable(na, nb, sol1, sol2):
	print ("input	a: " + na " b: " + nb)




main() #call main function