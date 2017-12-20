import pandas as pd
import numpy as np

f = {"name": ['A', 'B', 'C', 'D', 'A'],
      "price": [10, 12, 20, 30, None],
      "quantity": [90, 87, None, 45, 20],
      }
ff = pd.DataFrame(f, index=f['name'])

print (ff)
#   name  price  quantity
# A    A   10.0      90.0
# B    B   12.0      87.0
# C    C   20.0       NaN
# D    D   30.0      45.0
# A    A    NaN      20.0

print (ff.dropna())

print (ff.fillna(0)) # ff will NOT be modified
#   name  price  quantity
# A    A   10.0      90.0
# B    B   12.0      87.0
# C    C   20.0       0.0
# D    D   30.0      45.0
# A    A    0.0      20.0

# fill in specified values
d = {'price': 10, 'quantity': 40}
print (ff.fillna(d))

# fill in an specified random value
r1 = np.random.randint(10, 30, 1)[0]
r2 = np.random.randint(20, 90, 1)[0]
d = {'price': r1, 'quantity': r2}
print (ff.fillna(d))

# ffill: forward propagate
print (ff.fillna(method = 'ffill'))
#   name  price  quantity
# A    A   10.0      90.0
# B    B   12.0      87.0
# C    C   20.0      87.0
# D    D   30.0      45.0
# A    A   30.0      20.0

print (ff.fillna())