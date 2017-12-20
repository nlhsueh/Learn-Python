import numpy as np 

# TYPE
x = np.float32(1.0) 
print(type(x), np.ndim(x)) # <class 'numpy.float32'> 0

# n-dimention array
x = np.array(10)
print (type(x), np.ndim(x)) # <class 'numpy.ndarray'> 0

x = np.array([1,2])
print (type(x), np.ndim(x)) # <class 'numpy.ndarray'> 1

# ARRANGE
# [start, end) range
x = np.arange(1,10)
print (x) # [1 2 3 4 5 6 7 8 9]
print (x[0]) # [1]
print (x[2:4]) # [3 4]
print (x[-1]) # [9]
print (x[:-2]) # [1 2 3 4 5 6 7]

x = np.arange(1, 10, 2)
print (x) # [1 3 5 7]

x = np.array([np.arange(3), np.arange(3)])
print (x)
# [[0 1 2]
#  [0 1 2]]

np.arange(2, 6, dtype=np.float) 
# array([ 2.,  3.,  4.,  5.])

# RANDOM
a = np.random.random((2,3))
print (a)
# [[ 0.30808122  0.58282821  0.21773528]
#  [ 0.18894092  0.07991055  0.68953398]]

# ZERO
a = np.zeros((2, 3)) 
# array([[ 0.,  0.,  0.],
#        [ 0.,  0.,  0.]])

# ONE
b = np.ones((2,3))
print(b)
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

# FULL
c = np.full((2,3), 7) 
print(c) 
# [[7 7 7]
#  [7 7 7]]          

# EYE
d = np.eye(3) # 3*3 identity matrix
print(d)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# LINSPACE
e = np.linspace(-1, 1, 11)
print (e)
# [-1.  -0.8 -0.6 ...,  0.6  0.8  1. ]