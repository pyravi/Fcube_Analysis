import csv 
  
# field names 
fields = ['fullname','score','rst','speed','accuracy'] 
  
# data rows of csv file 
rows = [ ['Nikhil', '6000', '2', '9.0','10'],
         ['Sahil', '78000', '2', '9.1','10']] 
  
# name of csv file 
filename = "employee_birthday.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)
