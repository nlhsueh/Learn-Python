import matplotlib.pyplot as plt
import numpy as np

videos = [5,10,15,20,25,30,35,40]
grade =  [20,23,33,45,44,50,70,75]

# 23 表示 2*3 的方格, 1 表示在第 1 位置
plt.subplot(231) 
plt.scatter(videos, grade)

# 23 表示 2*3 的方格, 2 表示在第 2 位置
plt.subplot(232)    
plt.plot(videos, grade)

# 直方圖（Histogram）
plt.subplot(233) 
normal_samples = np.random.normal(size = 1000) 
uniform_samples = np.random.uniform(size = 1000)
plt.hist(normal_samples)
plt.hist(uniform_samples)

# 散佈圖, 點狀圖（Scatter plot）
plt.subplot(234) 
plt.scatter(videos, grade, c='b')

# 線圖（Line plot）
plt.subplot(235) 
plt.plot(videos, grade, c='y')

# 盒鬚圖（Box plot）
plt.subplot(236) 
plt.boxplot(normal_samples)

#plt.show()
plt.savefig('images/subplot.png')