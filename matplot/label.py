import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(25, 50, 100)
y = 2*x + 1

# using lim and label
plt.figure()
plt.title('demo xlim and xlabel')
plt.plot(x, y)
plt.xlim(20, 60)
plt.ylim(40, 120)
plt.xlabel("age")
plt.ylabel("week spend")
plt.savefig('images/label.png')

# using ticks
plt.figure()
plt.figure()
plt.title('demo ticks')
plt.plot(x, y)
plt.xlim(20, 60)
plt.ylim(40, 120)
plt.xlabel("age")
plt.ylabel("week spend")
age_ticks = np.linspace(25, 50, 5)
plt.xticks(age_ticks)
plt.yticks([50, 75, 100],
           ["eco", "normal", "waste"])
plt.savefig('images/ticks.png')
