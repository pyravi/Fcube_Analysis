import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')


#class formate in bar denoted
#sb.barplot(x = "sex", y = "survived", hue = "class", data = df)

#point denoting
sb.pointplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
