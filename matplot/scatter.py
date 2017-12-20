import matplotlib.pyplot as plt
import numpy as np

n = 1000    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

plt.title('Demo scatter')
plt.subplot(221)
plt.scatter(X, Y, s=30, alpha=.5)
plt.subplot(222)
plt.scatter(X, Y, s=3, alpha=.5)
plt.subplot(223)
plt.scatter(X, Y, s=3, alpha=.1)
plt.subplot(224)
plt.scatter(X, Y, s=3, alpha=1)

# s: size
# alpah: 透明度

#plt.show()
plt.savefig('images/scatter.png')