#!E:/Tools/Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
x =[1,2,3] #comments
y =[1,4,9]
z =[10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()
"""

sample_data =pd.read_csv('player.csv')
"""
print(sample_data)
show_type=type(sample_data)
print(show_type)
print(sample_data.speed)
print(sample_data.speed.iloc[1])
"""
y=sample_data.fullname
x=sample_data.score
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
