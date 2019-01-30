import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
#print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print(df)

#print(df[df.A > 0]) #compaire a particular columns
#print(df[df > 0]) #compaire all columns
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
#print(df2)
#print( df2[df2['E'].isin(['two','four'])]) #SELECT any particular values

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print(s1)
