#This script will grap the application banner from a target host

#import optparse module so we can get command line parameters
import optparse
#import socket so we can determine TCP/IP attributes
import socket
#import all funtions so that we don't need to type socket. in front of all of the function names
from socket import *

#Function to connect to a port and print if open or closed
def connScann(tgtHost, tgtPort):
	#try to run the scan
	try:
		#create a var from the socket object
		connSkt = socket(AF_INET, SOCK_STREAM)
		#make the connection to the target host/port
		connSkt.connect((tgtHost, tgtPort))
		#print out the if the port was open
		print '[+]%d/tcp open'% tgtPort
		#close the connection
		connSkt.close
	except:
		#print out if the port is closed
		print '[-]%d/tcp closed'% tgtPort

#function to scan the IP provided to the script
def portScan(tgtHost, tgtPorts):
	#try the socket function to get host by name (from hostname)
	try:
		#this will resolve hostname to IP address
		tgtIP = gethostbyname(tgtHost)
	except:
		#print that tgt host is not reachable
		print '[-] Cannot resolve "%s": Unknown host'%tgtHost
		return
	try:
		#var after resolving IP to host name
		tgtName = gethostbyaddr(tgtIP)
		#print the result of target name
		print'\n[+] Scan Results for: ' + tgtName[0]
	except:
		#print the IP address
		print'\n[+] Scan Results for: ' + tgtIP
	#set the socket default timeout
	setdefaulttimeout(1)
	#iterate through all tgt port
	for tgtPort in tgtPorts:
		#print the port you are about to scan
		print'Scanning port' + tgtPort
		#call the function that will scan the port
		connScann(tgtHost, int(tgtPort))
def main():
	#create parser for script parameters
	parser = optparse.OptionParser('usage%prog ' + '-H <target host> -p <target port>')
	#add the options 
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify the target port[s] separated by comma and no space example 21,80,25')
	#create the variable from the script parameters
	(options, args) = parser.parse_args()
	#create the tgtHost variable
	tgtHost = options.tgtHost
	#create the target ports variable
	print options.tgtPort
	tgtPorts = str(options.tgtPort).split(',')
	print tgtPorts
	#check if the variables have something in them
	if (tgtHost == None) | (tgtPorts[0] == None):
		#print error
		print '[-] You must specify a target host and port[s].'
		exit(0)
	#call the port scan function
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()