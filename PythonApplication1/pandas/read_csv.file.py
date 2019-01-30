""
s = pd.Series([1,3,5,np.nan,6,8])

print(s)
"""
dates = pd.date_range('20130101', periods=6)
#print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print(df)

df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.date_range('20130102', periods=4),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })

#print('Display the index, columns, and the underlying numpy data')
#print(df2.index,df2.columns,df.describe())
#print("Transposing your data")
#print(df2.T)
#print(df2.sort_index(axis=1, ascending=False))
#print(df2.sort_values(by='B'))

print('See the indexing documentation Indexing and Selecting Data'
 'and MultiIndex / Advanced Indexing')
#print(df2['B']) # access columns
#print(df2[0:3]) # access rows Selecting
"""
print(df.loc[dates[0]])
print(df.loc[:,['A','B']])
print(df.loc['20130102':'20130104',['A','B']])
print(df.loc['20130102',['A','B']])
print(df.at[dates[0],'A']) #printing scalar value
"""
print("""Select via the position of the passed integers""")
print(df)
#print(df.iloc[3])   # SELECT rows in all values
#print(df.iloc[3:5,0:2]) # SELECT rows of particular values
#print(df.iloc[[1,2,4],[0,2]]) #By lists of integer position locations, similar to the numpy/python style
#print(df.iloc[1:3,:]) #For slicing rows explicitly
#print(df.iloc[:,1:3]) #SELECTing columns
#print( df.iloc[1,1]) #For getting a value explicitly
#print(df.iat[1,1]) #For getting fast access to a scalar
