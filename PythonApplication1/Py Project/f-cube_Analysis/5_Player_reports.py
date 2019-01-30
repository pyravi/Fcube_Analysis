#!E:/Tools/Python
import csv
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()

Usr1 =input("Please provide Player Name:" 'First Player')
Usr2 =input("Please provide Player Name:" 'Second Player')
Usr3 =input("Please provide Player Name:" 'third Player')
Usr4 =input("Please provide Player Name:" 'fourth Player')
Usr5 =input("Please provide Player Name:" 'Fivth Player')

print("Top Score of Players {0}".format(Usr1,Usr2,Usr3,Usr4,Usr5))
test = """SELECT `full_name`,`cube_score`,`avg_rst`,`avg_accuracy`,`Avg_Speed` From `fcube_reports` \
WHERE full_name IN ('""" +Usr1+ """','""" +Usr2+ """','""" +Usr3+ """','""" +Usr4+ """','""" +Usr5+ """') \
 ORDER BY `fcube_reports`.`cube_score`  DESC LIMIT 5"""
query= test
try:
   cursor.execute(query)
   results= cursor.fetchall ()
   for row in results:
     print(row)

except:
   print ("Error: unable to fetch data")
mariadb_connection.close()
