import numpy as np
from sklearn import preprocessing
#We imported a couple of packages. Let's create some sample data and add the line to this file:
input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, -4.3]])

data_standardized = preprocessing.scale(input_data)
print(data_standardized)
#print ("\nMean =", data_standardized.mean(axis=0))
#print ("Std deviation =", data_standardized.std(axis=0))
