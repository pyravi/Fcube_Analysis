#!E:/Tools/Python
import mysql.connector as mariadb      # name of the library
import pandas as pd
import matplotlib.pyplot as plt
#Creating Pandas DataFrames & Selecting Data
#mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
#raw_data=pd.read_sql('SELECT *FROM employee',mariadb_connection)
#mariadb_connection.close()
#df=pd.DataFrame(raw_data)
#Columns=pd.Index(['emp_id','Emplyee_Name','Emplyee_BoD','Emplyee_salary'],Name='attributes'),Index=pandas.Index(['Emplyee_Name','Emplyee_salary'],Name='letter')
#df.show()

mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()
cursor.execute('SELECT full_name, cube_score, avg_rst, avg_accuracy, Avg_Speed, created FROM fcube_reports Limit 5 ')
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
value=df.rename(columns={0: 'full_name', 1: 'cube_score', 2: 'avg_rst', 3: 'avg_accuracy',4: 'Avg_Speed',5: 'created'}, inplace=True)
#df = df.sort_values(['cube_score'], ascending=[1])
#df.groupby('created')['full_name'].nunique().plot(kind='bar',rot=0)
myplot=df.plot(x='full_name', y=['cube_score','avg_rst','avg_accuracy','Avg_Speed'],kind="bar",rot=0, label=['cube_score','avg_rst','avg_accuracy','Avg_Speed'],title="Player cube_score Graph")
#plt.savefig('output.png')
plt.show()
