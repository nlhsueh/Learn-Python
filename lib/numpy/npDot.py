# DOT
import numpy as np

x = np.array([[1, 2],[3, 4]])
y = np.array([[5, 6],[7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors
print (v.dot(w)) # 219
print (np.dot(v, w)) # 219

# Matrix / vector product
print (x.dot(v)) # [29 67]
print (np.dot(x, v)) # [29 67]
print (v.dot(x)) # [39 58]

# Matrix / matrix product; both produce the rank 2 array
print (x.dot(y))
print (np.dot(x, y))
# [[19 22]
#  [43 50]]

# Elementwise * and Broadcasting, are different from dot
print (x*y) # element-wise *
print (x*v) # broadcasting

a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
print (a.dot(b))
b = np.arange(12).reshape(3,4)
print (a.dot(b)) # ERROR