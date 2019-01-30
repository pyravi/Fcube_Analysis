
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='root', password='', database='fcube')
cursor= mariadb_connection.cursor()

sql = "select fcube_reports.tfl_id, fcube_reports.full_name, fcube_reports.center_name, fcube_reports.age, fcube_reports.cube_score, fcube_reports.avg_rst, fcube_reports.Avg_Speed, fcube_reports.avg_accuracy, fcube_reports.created from fcube_reports \
        inner join users on fcube_reports.tfl_id = users.tfl_id \
        where users.fullname <> 'Demo Player' \
        and users.userType = 4 \
        AND users.profilestatus = 1 \
        AND users.epicentre NOT IN ('zawar','zawar mines','Hisar','kota','varanasi','jhajjar','Gawardi','Udaipur') \
        AND users.location NOT IN ('Hisar''kota','varanasi') \
        AND (fcube_reports.created >= '2018-10-01' and fcube_reports.created < '2018-12-01') \
        order by fcube_reports.full_name ASC"

query= sql
try:
   cursor.execute(query)
   results= cursor.fetchall ()
   for row in results:
     print(row)

except:
   print ("Error: unable to fetch data")
mariadb_connection.close()
