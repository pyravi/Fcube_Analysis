
#!E:/Tools/Python
import time
import sys
import mysql.connector as mariadb
start = time. time()
mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()
query= ("SELECT * FROM fcube_reports ORDER BY `full_name` ASC")

try:
    cursor.execute(query)
    results= cursor.fetchall ()
    for row in results:
        print(row)
except:
   print ("Error: unable to fetch data")
mariadb_connection.close()
end = time. time()
print(end - start)
sys.exit()
