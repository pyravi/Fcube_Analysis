import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
# only bin show
sb.distplot(df['petal_length'],kde = False)


#Kernel Density Estimation (KDE)show in cure wave
#sb.distplot(df['petal_length'],hist=False)
plt.show()
