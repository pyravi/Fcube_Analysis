#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb

cgitb.enable()

print "Content-Type:text/html"
#print "location: http://192.168.234.132/download.html"
print	
print "<form action=/cgi-bin/te.py>"
os.system("nmap 192.168.0.0/24 |grep report |cut -d' ' -f6|cut -d'(' -f2|cut -d')' -f1 > /var/www/cgi-bin/ip.txt")
f1=open("ip.txt","r+")
ipno=f1.readlines()
for i in range(0,len(ipno)):
	ipno[i]=ipno[i][:-1]
f1.close()
k=0
print "SELECT THE IP BELOW"
print "<br>"
print "<table> "
print "<form action=te.py>"
while len(ipno) != k :
	if ipno[k] != '' :
		print ipno[k]
		print "<input type='checkbox' name='ipt' value="+ipno[k]+">"	
		print "<input type='checkbox' name='ipd' value="+ipno[k]+">"	
		print "<input type='checkbox' name='ipj' value="+ipno[k]+">"	
		print "<input type='checkbox' name='ipn' value="+ipno[k]+">"	
		print "<br>"	
	k+=1
print "<input type=submit> "
