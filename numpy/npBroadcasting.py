import numpy as np

a = np.array([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ])
b = np.array([1, 2, 3])
print(a + b)
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]

# second way, if you do not use broadcasting
b2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print (a+b2)

# third way 
x = np.empty_like(a) # Create an empty matrix with the same shape as x
for i in range(3):
    x[i] = a[i] + b
print (x)

# broadcasting
print(a * b)

# application example
buy = np.array([[1, 1, 1],[2, 2, 2],[3, 3, 3]])

unitPrice = [100, 50, 10]
pay = np.dot(buy, unitPrice)
print (pay)
print (buy * unitPrice)

x = [[1, 1, 1],[2, 2, 2],[3, 3, 3]]
y = (x > 2)

y = buy > 2
print (y)
print (x[y])