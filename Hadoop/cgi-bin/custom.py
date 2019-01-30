#!/usr/bin/python

import commands
import operator
import sys
import cgi
import cgitb
cgitb.enable()
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]

print "Content-Type: text/html"

x=cgi.FormContent()
nn=x['nn'][0]
dn=x['dn']
jt=x['jt'][0]
tt=x['tt']
snn=x['snn'][0]
mp='devansh'
if snn in nn :
	print "location:http://"+k+"/cgi-bin/selectsnn.py"
	print	
elif snn in dn :
	print "location:http://"+k+"/cgi-bin/selectsnn.py"
	print	
elif nn in dn :
	print "location:http://"+k+"/cgi-bin/selectnn.py"
	print	
else :
	commands.getoutput("sudo mkdir /etc/hadoop/t")
	commands.getoutput("sudo mkdir /etc/hadoop/t/dn")
	commands.getoutput("sudo mkdir /etc/hadoop/t/snn")
	commands.getoutput("sudo mkdir /etc/hadoop/t/jt")

###########################Creating Namenode######################################################
	f8=open("/etc/hadoop/t/core-site.xml","w+")
	f8.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
	<!-- Put site-specific property overrides in this file. -->
	
	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://"""+nn+""":9001</value>
	</property>
	</configuration>""");
	f8.close()
	
	
	f9=open("/etc/hadoop/t/hdfs-site.xml","w+")
	f9.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
	<!-- Put site-specific property overrides in this file. -->
	
	<configuration>
	<property>
	<name>dfs.name.dir</name>
	<value>/namenode</value>
	</property>
	</configuration>""");
	f9.close()
	#commands.getoutput("sudo sshpass -p "+mp+" ssh "+nn+" setenforce 0")
	#commands.getoutput("sudo sshpass -p "+mp+" ssh "+nn+" iptables -F")
	commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/core-site.xml "+nn+":/etc/hadoop")
	commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/hdfs-site.xml "+nn+":/etc/hadoop")
	commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+nn+" hadoop namenode -format -y")
	#commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+nn+" hadoop-daemon.sh stop namenode")
	commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+nn+" hadoop-daemon.sh start namenode")
	#Creating Secondary Namenode###################################################
	f10=open("/etc/hadoop/t/snn/core-site.xml","w+")
	f10.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://"""+nn+""":9001</value>
	</property>
	</configuration>""");
	f10.close()
	f15=open("/etc/hadoop/t/snn/hdfs-site.xml","w+")
	f15.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>dfs.http.address</name>
	<value>"""+nn+""":50070</value>
	</property>
	<property>
	<name>dfs.secondary.http.address</name>
	<value>"""+snn+""":50090</value>
	</property>
	<property>
	<name>fs.checkpoint.dir</name>
	<value>/check</value>
	</property>
	<property>
	<name>fs.checkpoint.edits.dir</name>
	<value>/edits</value>
	</property>
	<property>
	<name>fs.checkpoint.period</name>
	<value>60</value>
	</property>
	</configuration>""");
	f15.close()

	commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/snn/core-site.xml "+snn+":/etc/hadoop")
	commands.getoutput("sudo sshpass -p "+mp+"  scp  /etc/hadoop/t/snn/hdfs-site.xml "+snn+":/etc/hadoop")
	commands.getoutput("sudo sshpass -p "+mp+" ssh "+snn+" hadoop-daemon.sh start secondarynamenode")

	################################################3creating jt##################33333
	f11=open("/etc/hadoop/t/jt/mapred-site.xml","w+")
	f11.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>mapred.job.tracker</name>
	<value>"""+jt+""":9002</value>
	</property>
	</configuration>""");
	f11.close()
	commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/jt/mapred-site.xml "+jt+":/etc/hadoop")
	commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+ jt+" hadoop-daemon.sh stop jobtracker")
	commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+ jt+" hadoop-daemon.sh start jobtracker")

	##################################################Creating Datanode###########################################################
	for i in dn:	
		f13=open("/etc/hadoop/t/dn/hdfs-site.xml","w+")
		f13.write("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

		<!-- Put site-specific property overrides in this file. -->

		<configuration>
		<property>
		<name>dfs.data.dir</name>
		<value>/dn</value>
		</property>
		</configuration>""");
		f13.close()
		#commands.getoutput("sudo sshpass -p "+mp+" ssh "+i+" setenforce 0")
		#commands.getoutput("sudo sshpass -p "+mp+" ssh "+i+" iptables -F")
		commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/core-site.xml "+i+":/etc/hadoop")
		commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/dn/hdfs-site.xml "+i+":/etc/hadoop")
		commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+i+" hadoop-daemon.sh stop datanode")
		commands.getoutput("sudo sshpass -p '"+mp+"' ssh "+i+" hadoop-daemon.sh start datanode")
	#######################################################Creating tasktrackers#########################################################
	for i in tt:
		#commands.getoutput("sudo sshpass -p "+mp+" ssh "+i+" setenforce 0")
		#commands.getoutput("sudo sshpass -p "+mp+" ssh "+i+" iptables -F")
		commands.getoutput("sudo sshpass -p "+mp+" scp  /etc/hadoop/t/jt/mapred-site.xml "+i+":/etc/hadoop")
		commands.getoutput("sudo sshpass -p "+mp+" ssh "+ i+" hadoop-daemon.sh stop tasktracker")
		commands.getoutput("sudo sshpass -p "+mp+" ssh "+ i+" hadoop-daemon.sh start tasktracker")
	print "location:http://"+k+"/op.html"
	print	

