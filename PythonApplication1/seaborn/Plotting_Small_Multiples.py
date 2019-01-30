import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
g = sb.FacetGrid(df, col = "sex", hue = "smoker")
#g.map(plt.scatter, "total_bill", "tip")
g.map(plt.hist, "tip")
plt.show()
