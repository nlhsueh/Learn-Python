import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y = x**3

# first figure
plt.figure(num=1, facecolor='red',figsize=(4,4))
    # num: figure id
    # facecolor: colore of the face 
    # figsize: size fo the figure

plt.title('face color')
plt.plot(x, y)
plt.savefig('images/figure1.png')

# second figure
plt.figure(num=2, figsize=(5,5))
plt.title('color, linewidth demo')
plt.plot(x, y, linewidth=10, color='y')
plt.plot(x, -1 * y)
plt.savefig('images/figure2.png')