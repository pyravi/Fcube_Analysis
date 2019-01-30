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
x=cgi.FormContent()
ch=x['cho'][0]
pas=x['pas'][0]
uid=x['uname'][0]
l=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
if uid in l :
	print "location: http://"+k+"/saasfa.html"
	print
	print ch
elif ch == '1':
	os.system('sudo useradd -s /usr/bin/firefox  '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >> /var/www/html/eror.txt" )
	fi=open('/var/www/html/cloud','w+')
	#fi=open('/var/www/cgi-bin/cloud','w+')
	fi.write("#!/usr/bin/python \nimport os \nos.system('ssh -X -l "+uid+"  "+k+ " firefox')\n")
	fi.close()
	fi=open('/var/www/html/client','w+')
	#fi=open('/var/www/cgi-bin/client','w+')
	fi.write("#!/usr/bin/python \nimport os\nos.system('chmod +x cloud') \nos.system('cp change.desktop /usr/share/applications/cloudfire.desktop')\n")
	fi.write("os.system('rm change.desktop')")
	os.system("cp change.desktop  /var/www/html/change.desktop")
	#os.system("cp cloudf"+uid+"  /var/www/html/cloud;cp clientf"+uid+"  /var/www/html/client")
	#os.system("sudo chmod 777 *")
	#os.system("tar -cvf cl.tar client cloud change.desktop >> /var/www/html/eror.txt")
	#os.system("sudo chmod 777 *")
	print "location: http://"+k+"/download.html"
	print
elif ch == '2':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >> /var/www/html/eror.txt" )
	fi=open('/var/www/html/cloud','w+')
	fi.write("#!/usr/bin/python \nimport os \nos.system('ssh -X -l "+uid+"  "+k+ " gcalctool ')\n")
	fi.close()
	fi=open('/var/www/html/client','w+')
	fi.write("#!/usr/bin/python \nimport os\nos.system('chmod +x cloud') \nos.system('cp change.desktop /usr/share/applications/cloudcal.desktop')\n")
	fi.write("os.system('rm change.desktop')")
	os.system("cp changec.desktop  /var/www/html/change.desktop")
	print "location: http://"+k+"/download.html"
	print	
elif ch == '3':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " | sudo passwd " +pas+ " --stdin >> /var/www/html/eror.txt" )
	fi=open('/var/www/html/cloud','w+')
	fi.write("#!/usr/bin/python \nimport os \nos.system('ssh -X -l "+uid+"  "+k+ " gnome-terminal ')\n")
	fi.close()
	fi=open('/var/www/html/client','w+')
	fi.write("#!/usr/bin/python \nimport os\nos.system('chmod +x cloud') \nos.system('cp change.desktop /usr/share/applications/cloudter.desktop')\n")
	fi.write("os.system('rm change.desktop')")
	os.system("cp changet.desktop  /var/www/html/change.desktop")
	print "location: http://"+k+"/download.html"
	print
elif ch == '4':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >> /var/www/html/eror.txt" )
	fi=open('/var/www/html/cloud','w+')
	fi.write("#!/usr/bin/python \nimport os \nos.system('ssh -X -l "+uid+"  "+k+ " wine Notepad ')\n")
	fi.close()
	fi=open('/var/www/html/client','w+')
	fi.write("#!/usr/bin/python \nimport os\nos.system('chmod +x cloudnote') \nos.system('cp change.desktop /usr/share/applications/rdcloudnotepad.desktop')\n")
	fi.write("os.system('rm change.desktop')")
	os.system("cp rdcloudnotepad.desktop  /var/www/html/change.desktop")
	print "location: http://"+k+"/download.html"
	print
elif ch == '5':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >> /var/www/html/eror.txt" )
	fi=open('/var/www/html/cloud','w+')
	fi.write("#!/usr/bin/python \nimport os \nos.system('ssh -X -l "+uid+"  "+k+ " wine wordPad ')\n")
	fi.close()
	fi=open('/var/www/html/client','w+')
	fi.write("#!/usr/bin/python \nimport os\nos.system('chmod +x cloudword') \nos.system('cp change.desktop /usr/share/applications/rdcloudwordpad.desktop')\n")
	fi.write("os.system('rm change.desktop')")
	os.system("cp rdcloudwordpad.desktop  /var/www/html/change.desktop")
	print "location: http://"+k+"/download.html"
	print

