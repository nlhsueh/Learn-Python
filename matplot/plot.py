import matplotlib.pyplot as plt
import numpy as np

# Example 1
plt.plot([1,2,3,4], [2,5,9,12])
plt.show()

# Example 2
x = np.linspace(-1, 1, 100)
y = x**2
plt.plot(x, y)
plt.show()

# Example 3- add title
plt.title('plot demo')
plt.plot(x, y)
plt.plot(x, x**3 - 0.5)
plt.grid()
plt.show()
plt.savefig('images/plot.png')

# Example 4- use subplots()
fig, ax = plt.subplots()
ax.plot(x, y)

fig, ax = plt.subplots()
ax.plot(x, y)