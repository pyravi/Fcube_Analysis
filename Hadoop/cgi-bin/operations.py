#!/usr/bin/python2
import commands
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"
print 

data = cgi.FormContent()
key=data.keys()[0]

if key =='direct':
	commands.getoutput("sudo hadoop fs -mkdir /"+data[key][0])

elif key == 'filep':
	commands.getoutput("sudo hadoop fs -put "+data[key][0]+" /")

elif key == 'dfile':
	commands.getoutput("sudo hadoop fs -rmr /"+data[key][0]+" /")

elif key == 'disfile':
	o=commands.getoutput("sudo hadoop fs -cat /"+data[key][0]+" /")
	print o

elif data.keys() == ['fname','oname']:
	commands.getoutput("sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /"+data['fname'][0]+" /"+data['oname'][0]) 
	p=commands.getoutput("sudo hadoop fs -cat /"+data['oname'][0]+"/part*")
	print p

'''fileput = data['filep'][0]
fildel = data['delfile'][0]
filedisp = data['dispfile'][0]
fname = data['fname'][0]
oname = data['oname'][0]

if len(directory) != 0 :
	commands.getoutput("sudo hadoop fs -mkdir /"+directory)
elif len(fileput) != "" :
	commands.getoutput("sudo hadoop fs -put "+fileput+" /")
elif len(fildel) != "" :
	commands.getoutput("sudo hadoop fs -rm /"+filedel+" /")
elif len(filedisp) != "":
	o=commands.getoutput("sudo hadoop fs -cat /"+filedisp+" /")
	print o
elif len(fname) != "" and len(oname) != "":
	commands.getoutput("sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /"+fname+" /"+oname) 
	p=commands.getoutput("sudo hadoop fs -cat /"+oname+"/part*")
	print p'''
