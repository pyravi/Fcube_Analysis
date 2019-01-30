import pandas as pd
filename = "output.csv"
#names = ['FirstName','Lastname','Email','Address','Username','password','userType','DOB','Location','BloodGrp','Gender','Epicenter','center','mobile','parentname','parentmobile','parentAddress','facebook','instagram','city','createdby']
dataset = pd.read_csv(filename)
print(dataset.head())
#print(dataset.shape)
#print(dataset.head(2))
#print(dataset.describe())
#print(dataset.groupby('cgpa').size())
