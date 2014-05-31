#compute the numeric value of a name 

def main():

	#get name
	name = (input("Please input name: ")).lower()

	#set var for total name value to 0
	total = 0
	#print(name) # for trouble shooting
	l = name.split()
	#loop through each letter and assign a value
	for i in l:
		for l in i:
			total = total + (ord(l) - 96)

	#print the total
	print(total)

main()

