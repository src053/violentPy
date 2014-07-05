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
def portScan(tgtHost, tgtPort):
	#try the socket function to get host by name (from hostname)
	try:
		#this will resolve hostname to IP address
		tgtIP = gethostbyname(tgtHost)
	except:
		#print that tgt host is not reachable
		print '[-] Cannot resolve '%s': Unknown host'%tgtHost
		return
	try:
		#this will resolve IP to host name
		tgtName = gethostbyaddr(tgtIP)

	except Exception, e:
		raise
	else:
		pass
	finally:
		pass

