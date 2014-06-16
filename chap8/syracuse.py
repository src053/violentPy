#a Program that finds the syracuse sequence

#function to call the even calculation
def even(n):
	return n/2
#function to call the odd calculation
def odd(n):
	return 3 * n + 1

def main():
	#get the natural number from user
	n = eval(input("Please enter a natural number: "))
	#iterate until the n var is 1
	while n > 1:
		#if n var is evenly divisible by two then run the even function
		if n % 2 == 0:
			#for trouble shooting
			print("even function will be ran")
			n = even(n)
			#print the value of n
			print(n)
		#if n var is odd then run the odd function
		else:
			n = odd(n)
			print(n)

main()