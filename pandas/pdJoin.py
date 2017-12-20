import pandas as pd

f = {"name": ['A', 'B', 'C', 'D'],
      "price": [10, 12, 20, 30],
      "quantity": [90, 87, 23, 45],
      }

ff = pd.DataFrame(f, index = f['name'])

s = {"name": ['A', 'B', 'C', 'F'],
      "weight": [10, 12, 20, 30],
      "size": [1, 1, 2, 3],
      }

ss = pd.DataFrame(s, index = f['name'])

j = pd.concat((ff, ss)) # implicit outer join
print (j)
#   name  price  quantity  size  weight
# A    A   10.0      90.0   NaN     NaN
# B    B   12.0      87.0   NaN     NaN
# C    C   20.0      23.0   NaN     NaN
# D    D   30.0      45.0   NaN     NaN
# A    A    NaN       NaN   1.0    10.0
# B    B    NaN       NaN   1.0    12.0
# C    C    NaN       NaN   2.0    20.0
# D    F    NaN       NaN   3.0    30.0

m = ff.merge(ss)
print (m)
#   name  price  quantity  size  weight
# 0    A     10        90     1      10
# 1    B     12        87     1      12
# 2    C     20        23     2      20

m2 = ff.merge(ss, how='left')
print (m2)
#   name  price  quantity  size  weight
# 0    A     10        90   1.0    10.0
# 1    B     12        87   1.0    12.0
# 2    C     20        23   2.0    20.0
# 3    D     30        45   NaN     NaN