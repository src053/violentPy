#program to create acronyms

def main():

	#Input phrase
	phrase = input("Please enter a short phrase: ")
	split = phrase.split()

	#acronym var
	acro = ""

	#Loop through phrase and grap the first letter of each word
	for word in split:
		acro = acro + word[0].upper()

	#print the acronym
	print(acro)

main()
