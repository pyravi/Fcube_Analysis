#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb
cgitb.enable()

print "Content-type:text/html"



cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
f1=open('/etc/hadoop/core-site.xml','w')
f1.write("<?xml version=\"1.0\"?> \n <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n <!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+k+":9001</value>\n</property>\n</configuration>")
f1.close()
f1=open('/etc/hadoop/hdfs-site.xml','w')
f1.write("<?xml version=\"1.0\"?> \n <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n <!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/naame</value>\n</property>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/daaa</value>\n</property>\n</configuration>")
f1.close()
f1=open('/etc/hadoop/mapred-site.xml','w')
f1.write("<?xml version=\"1.0\"?> \n <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n <!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+k+":9002</value>\n</property>\n</configuration>")
f1.close()
commands.getoutput("sudo hadoop namenode -format -y")
commands.getoutput("sudo hadoop-daemon.sh stop namenode")
commands.getoutput("sudo hadoop-daemon.sh stop jobtracker")
commands.getoutput("sudo hadoop-daemon.sh stop tasktracker")
commands.getoutput("sudo hadoop-daemon.sh stop datanode")
commands.getoutput("sudo hadoop-daemon.sh start namenode")
commands.getoutput("sudo hadoop-daemon.sh start jobtracker")
commands.getoutput("sudo hadoop-daemon.sh start tasktracker")
commands.getoutput("sudo hadoop-daemon.sh start datanode")
print "location:http://"+k+"/op.html"
print	

		
