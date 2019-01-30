import mysql.connector as mariadb
import pandas as pd
import csv
import matplotlib.pyplot as plt

mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()

cursor.execute('SELECT full_name, cube_score, avg_rst, avg_accuracy, Avg_Speed, created FROM fcube_reports Limit 10 ')
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
# field names
fields = ['full_name','cube_score','avg_rst','avg_accuracy','Avg_Speed','created']
# name of csv file
filename = "usr_file.csv"
# writing to csv file
with open(filename, 'w') as csvfile:
# creating a csv writer object
    csvwriter = csv.writer(csvfile)
# writing the fields
    csvwriter.writerow(fields)
# writing the data rows
    csvwriter.writerows(rows)

df.rename(columns={0: 'full_name', 1: 'cube_score', 2: 'avg_rst', 3: 'avg_accuracy',4: 'Avg_Speed',5: 'created'}, inplace=True)
df = df.sort_values(['cube_score'], ascending=[1])

census_data = pd.read_csv('usr_file.csv')
ts=census_data[1:2]
"""
df = pd.DataFrame(ts, index=ts.index,columns=['full_name', 'cube_score', 'avg_rst', 'avg_accuracy','Avg_Speed'])
df.plot(); plt.legend(loc='best')
plt.show()
"""
a = pd.DataFrame({'Player Evalution':['cube_score', 'avg_rst', 'avg_accuracy','Avg_Speed'], 'val':[402.0,5.39,4.33,20.64706]})
ax=a.plot.bar(x='Player Evalution', y='val', rot=0)
plt.show()
