"""
==================
Multiple lines
==================

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y_1 = np.sin(4 * np.pi * x) * np.exp(-5 * x)
y_2 = np.sin(3 * np.pi * x) * np.exp(-2 * x)

fig, ax = plt.subplots()

ax.plot(x,y_1, label='y=4*pi*x*-5^x', linestyle='dashed', color='c')
ax.plot(x,y_2, label='y=3*pi*x*-2^x', linestyle='dotted', color='m')
ax.grid(True, zorder=5)

ax.annotate('Minimum',
            xy=(0.48, -0.38), xycoords='data',
            xytext=(10, 50), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')



plt.legend()
plt.show()