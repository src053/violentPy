#This script will be used to find the password of a zip file using a dictionary input file

import zipfile #module containing zip functionality
import optparse #module containing option parsing of script
from threading import Thread #import thread function from threading module

#Function for extracting zip file
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password) #call the extract function on the zipped file
		print '[+] Found password' + password + '\n'
	except:
		pass

def main():
	parser = optparse.OptionParser("usage prog " + "-f <zipfile> -d <dictionary>") #This give the example of how to use the options
	parser.add_option('-f', dest='zname', type='string', help='specify zip file') #defines the -f function
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file') #defines what the -d parameter does and what variable it goes to
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None): #check if the parameters have been provided
		print parser.usage #if not then print out the proper usage of the script
		exit(0)
	else:
		zname = options.zname #create var with the -f parameter value
		dname = options.dname #create var with the -d parameter value
	zfile = zipfile.ZipFile(zname) #create zipfile object
	passFile = open(dname) #create file object

	#iterate through the dictionary file
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start():

if __name__ == '__main__':
	main()
