#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb
cgitb.enable()
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
print "Content-Type:text/html"
print 
#os.system("sudo nmap "+k+"/24 |grep report |cut -d' ' -f6 |cut -d'(' -f2|cut -d')' -f1 >/var/www/cgi-bin/ip.txt")
os.system("sudo nmap "+k+"/24 |grep report |cut -d' ' -f5 >/var/www/cgi-bin/ip.txt")
f1=open("/var/www/cgi-bin/ip.txt","r+")
ip=f1.readlines()
for i in range(0,len(ip)):
	ip[i]=ip[i][:-1]
f1.close()
n=len(ip)
print "<form action=/cgi-bin/custom.py>"
print "<table style='border-width:4px'>"
print "<tr><td>LIST OF IP</td><td colspan=5>SELECT IP FOR RESPECTIVE</td></tr>"
print "<tr><td colspan=6> SELECT A UNQUIE  SECONDARYNAMENODE</td></tr>"
print "<tr><td></td><td>NAME NODE</td><td>DATA NODE</td><td>JOB TRACKER</td><td>TASK TRACKER</td><td>SECONDRY NAME NODE</td></tr>"
print "<tr><td>"+k+"</td><td><input type=radio name=nn value="+k+"></td><td><input type=checkbox name=dn value="+k+"></td><td><input type=radio name=jt value="+k+"></td><td><input type=checkbox name=tt value="+k+"></td><td><input type=radio name=snn value="+k+"></td></tr>"
for i in range(0,len(ip)) :
	if ip[i] != '' and ip[i] != "192.168.126.1" and ip[i] != "192.168.126.2" and ip[i] != "192.168.126.254" and ip[i] != "main":
		print "<tr><td>"+ip[i]+"</td><td><input type=radio name=nn value="+ip[i]+"></td><td><input type=checkbox name=dn value="+ip[i]+"></td><td><input type=radio name=jt value="+ip[i]+"></td><td><input type=checkbox name=tt value="+ip[i]+"></td><td><input type=radio name=snn value="+ip[i]+"></td></tr>"

print "<tr><td><input type=submit value='create cluster'></td></tr>"
print "</table></form>"


