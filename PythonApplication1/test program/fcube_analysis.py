import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
size = 0.3
size1= 0.33

#vals = np.array([[29., 10.],[29., 10.], [29., 10.],[29., 10.]])
vals = np.array([[59., 10.]])
vals1 = np.array([[59., 10.]])
vals2 = np.array([[29., 10.]])
vals3 = np.array([[59., 10.]])


cmap = plt.get_cmap("tab20b")
cmap1 = plt.get_cmap("tab20")
cmap2 = plt.get_cmap("tab10")
cmap3 = plt.get_cmap("tab20b")
outer_colors = cmap(np.arange(1)*4)
outer_colors1 = cmap1(np.arange(1)*4)
outer_colors2 = cmap(np.arange(1)*4)
outer_colors3 = cmap1(np.arange(1)*4)
#inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
ax.pie(vals.sum(axis=1), radius=1.0, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
ax.pie(vals1.sum(axis=1), radius=1-size, colors=outer_colors1,
       wedgeprops=dict(width=size1, edgecolor='w'))
ax.pie(vals2.sum(axis=1), radius=1.2, colors=outer_colors2,
       wedgeprops=dict(width=size, edgecolor='w'))
""""
ax.pie(vals3.sum(axis=1), radius=1.3, colors=outer_colors3,
       wedgeprops=dict(width=size, edgecolor='w'))"""

#ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       #wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Player Analysis reports')
plt.show()
