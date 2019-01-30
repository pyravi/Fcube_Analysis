import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()
query1= 'Select @@version'
#query2='SELECT VERSION()'
try:
   cursor.execute(query1)
   #cursor.execute(query2)
   results= cursor.fetchall ()
   #result= cursor.fetchone()
   #print ("database version %s:" %result)
   for row in results:
     print(row)

except:
   print ("Error: unable to fetch data")
   mariadb_connection.close()
