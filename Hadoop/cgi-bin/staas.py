#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import crypt
import cgitb

cgitb.enable()

print "Content-Type:text/html"
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
x=cgi.FormContent()
n=x['size'][0]
ch=x['cho'][0]
pas=x['pas'][0]
uid=x['uname'][0]
l=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")

if (uid in l) and ch < 4 :
	print "location: http://"+k+"/STAASFA.html"
	print

elif ch == '1':
	ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= ce[1]:
		print
		print ce[1]+n
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system('sudo useradd '  +uid)
		os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >>/var/www/html/gc.txt" )
		os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1 >>/var/www/html/gc.txt")
		os.system("sudo mkfs.vfat /dev/vg1/"+uid+" >>/var/www/html/gc.txt")
		os.system("sudo mkdir /staaso/"+uid)
		os.system("sudo mount /dev/vg1/"+uid+" /staaso/"+uid)
		f1=open('/etc/exports','a')
		f1.write("\n/staaso/"+uid+ " *(rw,no_root_squash)\n")
		f1.close()
		os.system("sudo /etc/init.d/nfs restart  >>/var/www/html/gc.txt")
		f1=open('/var/www/html/staasoclient','w+')
		f1.write("#!/usr/bin/python \nimport os \nos.system('mkdir /media/rdbox')\nos.system('mount "+k+":/staaso/"+uid+" /media/rdbox')")
		f1.close()
		os.system('chmod +x /var/www/html/staasoclient')		
		print "location: http://"+k+"/downloads.html"
		print	
elif ch == '2':
	ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= ce[1]:
		print		
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system('sudo useradd '  +uid)
		os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >>/var/www/html/gc.txt" )
		os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1 >>/var/www/html/gc.txt")
		os.system("sudo mkfs.vfat /dev/vg1/"+uid+" >>/var/www/html/g1c.txt")
		os.system("sudo mkdir /staaso/"+uid)
		os.system("sudo mount /dev/vg1/"+uid+" /staaso/"+uid)
		os.system("sudo chown "+uid+ " /staaso/"+uid)
		os.system("sudo yum install sshfs -y >>/var/www/html/gc.txt")
		os.system("sudo service sshd restart >>/var/www/html/gc.txt")
		f1=open('/var/www/html/staasoclient','w+')
		f1.write("#!/usr/bin/python \nimport os \nos.system('mkdir /media/rdbox')\nos.system('sshfs "+uid+"@"+k+":/staaso/"+uid+" /media/rdbox')")
		f1.close()
		#os.system('sudo chmod +x staasoclient')			
		print "location: http://"+k+"/downloads.html"
		print	
elif ch == '3':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +pas+ " --stdin >>/var/www/html/gc.txt" )
	os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1  >>/var/www/html/gc.txt")
	os.system("sudo yum install scsi-target-utils  >>/var/www/html/gc.txt")
	fi=open('/etc/tgt/target.conf','a')		
	fi.write("\n<target mystore"+uid+"> \n backing-store /dev/vg1/"+uid+"\n</target>\n")	
	fi.close()	
	os.system("sudo setenforce 0;sudo iptables -F;")
	os.system("sudo service tgtd restart  >>/var/www/html/gc.txt")
#	iqn=commands.getoutput("cat /etc/iscsi/initiatorname.iscsi |cut -d= -f2")
	fc=open('/var/www/html/staasoclient','w+')
	fc.write("#!/usr/bin/python\nimport commands\n\nimport os\n\nos.system(\"yum install iscsi-initiator-utils;iscsiadm --mode discoverydb --type sendtargets --portal "+k+" --discover;iscsiadm --mode node --targetname mycloudiqn --portal "+k+":3260 --login\")")
	fc.close()			
	print "location: http://"+k+"/downloads.html"
	print	
elif ch == "4" :
	if uid in l :
		a=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f3")
		y=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f2")
		b=crypt.crypt(""+pas+"","$"+y+"$"+a+"$")
		if b == commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+" |cut -d: -f2") :
			ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
			if n >= ce[1]:
				print 
				print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
			else :
				os.system("sudo lvextend --size +"+str(n)+"G /dev/vg1/"+uid+ "  >>/var/www/html/gqc.txt")
				os.system("sudo resize2fs /dev/vg1/"+uid+"  >>/var/www/html/gc.txt")
				print 
				print "SUCCESSFULL INCREASED"

		else :
			print 
			print "Enter a VAlid pas"	
	else:
		print 
		print "Enter a Valid USErname"
elif ch == "5" :
	if uid in l :
		a=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f3")
		y=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f2")
		b=crypt.crypt(""+pas+"","$"+y+"$"+a+"$")
		if b == commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+" |cut -d: -f2") :
			ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
			if n >= ce[1]:
				print 
				print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
			else :
				os.system("sudo umount  /dev/vg1/"+uid)
				#os.system("sudo e2fsck -f /dev/vg1/"+uid)
				#os.system("sudo resize2fs /dev/vg1/"+uid)
				os.system("sudo echo -e 'y\n' |sudo lvreduce --size "+str(n)+"G /dev/vg1/"+uid+ " >>/var/www/html/gc.txt" )
				os.system("sudo mount /dev/vg1/"+uid+" /staaso/"+uid)
				print 
				print "SUCCESSFULLY REDUCED"
		else :
			print 
			print "Enter a VAlid pas"	
	else:
		print 
		print "Enter a Valid USErname"
	
