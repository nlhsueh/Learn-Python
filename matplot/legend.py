import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(25, 50, 100)
ct1 = 2*x + 1
ct2 = 3*(x-4) - 20

plt.title('demo ticks')
# legend
plt.plot(x, ct1, label='city1')
plt.plot(x, ct2, label='city2')
plt.legend(loc='upper right')
plt.xlim(20, 60)
plt.ylim(40, 120)
plt.xlabel("age")
plt.ylabel("week spend")
age_ticks = np.linspace(25, 50, 5)
plt.xticks(age_ticks)
plt.yticks([50, 75, 100],
           ["eco", "normal", "waste"])
#plt.show()
plt.savefig('images/legend.png')
""" Legend location
'best' : 0,
'upper right'  : 1,
'upper left'   : 2,
'lower left'   : 3,
'lower right'  : 4,
'right'        : 5,
'center left'  : 6,
'center right' : 7,
'lower center' : 8,
'upper center' : 9,
'center'       : 10,
"""