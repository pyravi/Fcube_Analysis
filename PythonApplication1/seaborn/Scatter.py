import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df)

#hex formate in show
#sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind = 'hex')
#kde formate in show
#sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind = 'kde')
plt.show()
