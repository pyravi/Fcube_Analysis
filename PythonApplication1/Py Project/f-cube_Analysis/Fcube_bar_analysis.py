import mysql.connector as mariadb
import pandas as pd
import matplotlib.pyplot as plt

mariadb_connection = mariadb.connect(user='root', password='', database='fcubedb')
cursor= mariadb_connection.cursor()
cursor.execute('SELECT full_name, cube_score, avg_rst, avg_accuracy, Avg_Speed, created FROM fcube_reports order by cube_score DESC')
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
"""value=df.rename(columns={0: 'full_name', 1: 'cube_score', 2: 'avg_rst', 3: 'avg_accuracy',4: 'Avg_Speed',5: 'created'}, inplace=True)
#df = df.sort_values(['cube_score'], ascending=[1])
#df.groupby('created')['full_name'].nunique().plot(kind='bar',rot=0)
myplot=df.plot(x='full_name', y=['cube_score','avg_rst','avg_accuracy','Avg_Speed'],kind="bar",rot=0, label=['cube_score','avg_rst','avg_accuracy','Avg_Speed'],title="Player cube_score Graph")
#plt.savefig('output.png')
"""

print(df.loc[1:5])
#print(dataset.groupby('cgpa').size())
"""
# Create bars
barWidth = 0.9
bars1 = [3, 3, 1]
bars2 = [4, 2, 3]
bars3 = [4, 6, 7, 10, 4, 4]
bars4 = bars1 + bars2 + bars3
# The X position of bars
r1 = [1,5,9]
r2 = [2,6,10]
r3 = [3,4,7,8,11,12]
r4 = r1 + r2 + r3
# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='Alone')
plt.bar(r2, bars2, width = barWidth, color = (0.3,0.5,0.4,0.6), label='With Himself')
plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4,0.6), label='With other genotype')
# Note: the barplot could be created easily. See the barplot section for other examples.
# Create legend
plt.legend()
# Text below each barplot with a rotation at 90°
plt.xticks([r + barWidth for r in range(len(r4))], ['DD', 'with himself', 'with DC', 'with Silur', 'DC', 'with himself', 'with DD', 'with Silur', 'Silur', 'with himself', 'with DD', 'with DC'], rotation=90)
# Create labels
label = ['n = 6', 'n = 25', 'n = 13', 'n = 36', 'n = 30', 'n = 11', 'n = 16', 'n = 37', 'n = 14', 'n = 4', 'n = 31', 'n = 34']
# Text on the top of each barplot
for i in range(len(r4)):
    plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 6)
# Adjust the margins
plt.subplots_adjust(bottom= 0.2, top = 0.98)
# Show graphic
plt.show()
"""
