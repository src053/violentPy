#simple program to impor a file with banner names


import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2) #define the default time out for socket object to two seconds
		s = socket.socket() #create a var with socket object
		s.connect((ip,port)) #connect to the ip and port with socket object
		banner = s.recv(1024) #create var of the first 1024 bytes found on the connection
		return banner
	except:
		return # return nothing if there is no connection

def checkVulns(banner, filename):
	f = open(filename, 'r') #open the file with banner names
	for line in f.readlines(): #iterate each line in the file
		if line.strip('\n') in banner:
			print '[+] Server is vulnerable: ' + banner.strip('\n')

def main():
	if len(sys.argv) == 2: #check for parameter from script
		filename = sys.argv[1] #create the var containint the filename from input
		if not os.path.isfile(filename): #check if the path exists
			print '[-] ' + filename + ' does not exist' #print an error
			exit(0) #exit the script
		if not os.access(filename, os.R_OK): #check if the file is readable
			print '[-] ' + filename + ' access denied.' #print an error
			exit(0) #exit the script
	elif len(sys.argv) == 1:
		print 'in the elif loop'
		print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
		exit(0)

	else:
		print 'program still going'
		portList = [21,22,25,80,110,443]
		for x in range(147, 150):
			print 'in the range loop'
			ip = '192.168.95.' + str(x)
			for port in portList:
				banner = retBanner(ip, port)
				if banner:
					print '[+] ' + ip + ': ' + banner
					checkVulns(banner, filename)
if __name__ == '__main__':
	main()
