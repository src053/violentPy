#A simple program illustration chaotic behavior.
#Example from Python programing
def showGrid(n, firstForm, secondForm, firstDisplay, secondDisplay):
	print("formula	  " + str(firstForm) + "		" + str(secondForm))
	print("------------------------------")
	for i in range(n):
		one = str(firstDisplay[i])
		two = str(secondDisplay[i])
		print("          " + one + "          " + two)

def exp1(x, n): #first algebric expression
	print("We will use formula 3.9 * x * (1 - x)")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * x * (1 - x) #re-define the x var with new assignment
		print (x) #print the value of x to user
		li.append(x)
	print(li)
	return li

def exp2(x, n): #second algebric expression
	print("We will use formula 3.9 * (x - x * x)")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * (x - x * x) #re-define the x var with new assignment
		print (x) #print the value of x to user
		li.append(x)
	print(li)
	return li

def exp3(x, n): #Third algebric expression
	print("We will use formula 3.9 * x - 3.9 * x * x")
	li = []
	for i in range(n): # loop n times with the for loop
		x = 3.9 * x - 3.9 * x * x #re-define the x var with new assignment
		print (x) #print the value of x to user
		li.append(x)
	print(li)
	return li

def main(): # define the function main
	print ("this program illustrates a caotic function") #print somethign to the user
	x = eval(input("Enter a number between 0 and 1: ")) #print question to user then assign the input to x var
	n = eval(input("How many numbers should I print? ")) #print question to user then assign how many numbers to print
	num1 = eval(input("Choose the first algebraic formula would you like to use? Choose 1, 2, or 3: ")) #print question to user then assign the chaotic formula to use
	num2 = eval(input("Choos the second algebraic formula would you like to use? Choose 1, 2, or 3: "))

	if num1 == 1 and num2 == 2: #decide if the two formula's are one and two
		ans1 = exp1(x, n) #Call the exp1 function and put results in the ans1 var
		ans2 = exp2(x, n)
	elif num1 == 1 and num2 == 3:
		ans1 = exp1(x, n)
		ans2 = exp3(x, n)
	elif num1 == 2 and num2 == 1:
		ans1 = exp2(x, n)
		ans2 = exp1(x, n)
	elif num1 == 2 and num2 == 3:
		ans1 = exp2(x, n)
		ans2 = exp3(x, n)
	elif num1 == 3 and num2 == 1:
		ans1 = exp3(x, n)
		ans2 = exp1(x, n)
	else:
		ans1 = exp3(x, n)
		ans2 = exp2(x, n)

	showGrid(n, num1, num2, ans1, ans2)

main() #call main function