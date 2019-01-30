#!E:/Tools/Python
import mysql.connector as mariadb
import time

start=time.time()
mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()

query= ("SELECT full_name,center_name,age,avg_rst,avg_accuracy,Avg_Speed,cube_score FROM fcube_reports ORDER by full_name")

cursor.execute(query)
result= cursor.fetchall()
for row in result:
     print(row)
mariadb_connection.close()
end=time.time()
print(end - start)
