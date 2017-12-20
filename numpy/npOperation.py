import numpy as np

# +-*/
a = np.arange(5) 
b = np.arange(5) 
c = a + b 
print (c) # [0 2 4 6 8]
c = a - b
print (c) # [0 0 0 0 0]
c = a * b 
print (c) # [0 1 4 9 16]
c = a**3
print (c) # [0 1 8 27 64]

c = a > 3
print (c) # [False False False False True]

# reshape
a = np.arange(6).reshape(2,3)
print (a) 
# [[0 1 2]
#  [3 4 5]]
print (a[0]) # [0 1 2]
print (a[0, 1]) # 1
print (a[0, 1:3]) # [1 2]

# MEAN, MIN, MAX
a = np.array([[34, 12, 90], [20, 56, 90], [45, 56, 92], [1, 2, 3]])
print ('min and max: ', np.min(a), a.max())
print ('mean: ', a.mean())
print ('column mean: ', a.mean(axis = 0))
print ('row mean: ', a.mean(axis = 1))
print ('sort: ', np.sort(a))

p = a > 60
print (p)

a[a > 60]

# transport
a = np.array([[34, 12, 90], [20, 56, 90], [45, 56, 92], [1, 2, 3]])
print (a.T)
# [[34 20 45  1]
#  [12 56 56  2]
#  [90 90 92  3]]