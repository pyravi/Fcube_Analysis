#!E:/Tools/Python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()
cursor.execute("SELECT VERSION()")
result= cursor.fetchone()
print ("database version %s:" %result)
mariadb_connection.close()
