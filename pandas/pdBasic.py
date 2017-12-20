import pandas as pd
a = pd.Series([11, 28, 72, 3, 5, 8])
print (a)
print (a.index)
print (a.values)

fruit = ['A', 'B', 'C']
price = [10, 23, 30]
a = pd.Series(price, index=fruit)
print (a)

fruit2 = ['A', 'D']
b = pd.Series([20, 1], fruit2)
print (a+b)

print (a['A'])
print (a[['A', 'B']])

print (a * 1.3 + 10)

import numpy as np
np.sin(a)

# Series.apply(func, convert_dtype=True, args=(), **kwds)
a.apply(np.sin)
a.apply(lambda x: x if x > 20 else x+10 )

a[a>20]

# dictionary
b= {'A': 10, 'B': 20, 'C': 30}
c = pd.Series(b)
print (c)

# Fill in 
fruit = ['A', 'B', 'C', 'D']
a = pd.Series([10, 20, None , 30], fruit)
print (a)
print (a.fillna(0))