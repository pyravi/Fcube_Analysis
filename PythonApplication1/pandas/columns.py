import os
import pandas as pd
filename='E:/Devops/PythonApplication1/pandas/output.csv'
df = pd.read_csv(filename)

for col in df.columns:
    series = df[col]
    print(series)
