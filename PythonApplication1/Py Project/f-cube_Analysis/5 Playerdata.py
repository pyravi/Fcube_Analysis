#!E:/Tools/Python
import mysql.connector as mariadb
import matplotlib.pyplot as plt
mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor(buffered=True)
#declear of user
Player1 =input("Please provide Username: " 'First Player ')
Player2 =input("Please provide Username: " 'Second Player ')
Player3 =input("Please provide Username: " 'third Player ')
Player4 =input("Please provide Username: " 'fourth Player ')
Player5 =input("Please provide Username: " 'Fivth Player ')

#intilazation for SQL Query
test = """SELECT full_name,cube_score,avg_rst,avg_accuracy,Avg_Speed From `fcube_reports`\
 WHERE full_name IN ('""" +Player1+ """','""" +Player2+ """','""" +Player3+ """','""" +Player4+ """','""" +Player5+ """') \
 ORDER BY `fcube_reports`.`cube_score`  DESC """
query=test
try:
   cursor.execute(query)
   results= cursor.fetchall ()
   print("Your want to see five player data {0}".format(Player1,Player2,Player3,Player4,Player5),cursor.rowcount)
   for row in results:
      print(row) 
except:
   print ("Error: unable to fetch data")
finally:
      if (mariadb_connection.is_connected()):
         cursor.close()
         mariadb_connection.close()
         #print("connection is closed")
