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
print	
print
print "hello"
x=cgi.FormContent()
n=x['ipl'][0:]
for i in range(0,len(n)) :
	print n[i]
	print "<br/>"


