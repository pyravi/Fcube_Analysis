import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
g = sb.PairGrid(df)
#g.map(plt.scatter);
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter);
plt.show()
