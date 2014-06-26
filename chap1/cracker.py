#A program to crack hash on posix

#module to encrypt a string
import crypt

#function to test the password
def testPass(cryptPass):
	#var containing first two characters of the encrypted password, these characters are the salt
	salt = cryptPass[0:2]
	#var containing the dictionary.txt file
	dictFile = open('dictionary.txt', 'r')
	#iterate through the each line in the dictionary file
	for word in dictFile.readlines():
		#var with carae return removed in the line
		word = word.strip('\n')
		#var containing a hash of the word from dictionary
		cryptWord = crypt.crypt(word, salt)
		#test if the the hashed dictionary word matches the hash found in the user file
		if (cryptWord == cryptPass):
			#print out the password
			print '[+] Found Password: ' + word + '\n'
			#return to main program
			return
	#if you no match is found then print that it wasn't found
	print '[-] Password Not Found. \n'
	#return to main program
	return

def main():
	#var containing the user name and hashed password
	passFile = open('passwords.txt')
	#iterate through each line in the file
	for line in passFile.readlines():
		#if the line has a : then look for user name and hashed password
		if ":" in line:
			#var containing the user name
			user = line.split(':')[0]
			#var containing the hashed password with space removed from the back
			cryptPass = line.split(':')[1].strip(' ')
			#print out user who is being cracked
			print '[*] Cracking Password For: ' + user
			#run the testPass function to test all dictionary values
			testPass(cryptPass)
#test to make sure the file has a main
if __name__ == "__main__":
	main()
