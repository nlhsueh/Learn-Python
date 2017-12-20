import pandas as pd

f = {"name": ['A', 'B', 'C', 'D'],
      "price": [10, 12, 20, 30],
      "quantity": [90, 87, 23, 45],
      }

ff = pd.DataFrame(f)
print (ff)

ff = pd.DataFrame(f, index=f['name'])
print (ff)

ff = pd.DataFrame(f)
ff2 = ff.set_index('name')
print (ff2)

# custom index
ff = pd.DataFrame(f, index=['a', 'b', 'c', 'd'])
print (ff)

# rearranging the Order of Columns
ff = pd.DataFrame(f, 
                  columns = ['name', 'quantity', 'price'], 
                  index=['a', 'b', 'c', 'd'])
print (ff)

print (ff.name, ff.price, ff['quantity'])

# change value
ff.price = 10
print (ff.price)
ff.price = [10, 12, 20, 30]
print (ff.price)

# sum and cumsum
print (ff['quantity'].sum())
print (ff['quantity'].cumsum())

# add a new column and set value
f = {"name": ['A', 'B', 'C', 'D'],
      "price": [10, 12, 20, 30],
      "quantity": [90, 87, 23, 45],
      }
ff = pd.DataFrame(f, index=f['name'])

q = pd.Series([1, 2, 3, 2], index = f['name'])
ff['quality'] = q # quality is a new column (field)
print (ff)

# replace values
f = {"name": ['A', 'B', 'C', 'D'],
      "price": [10, 12, 20, 30],
      "quantity": [90, 87, 23, 45],
      }
ff = pd.DataFrame(f, index=f['name'])

q = pd.Series([11, 21, 31, 21], index = f['name'])
ff['price'] = q
print (ff)

# SELECT COLUMNs
cf = pd.DataFrame(f, columns=['quantity', 'cum quantity'], 
                    index = f['name'])
print (cf)

cf['cum quantity'] = cf['quantity'].cumsum()
print (cf)

# SELECT ROWs
f = {"name": ['A', 'B', 'C', 'D', 'A'],
      "price": [10, 12, 20, 30, 40],
      "quantity": [90, 87, 23, 45, 20],
      }
ff = pd.DataFrame(f, index=f['name'])

# loc will select a specifc row
print (ff.loc['A'])
print (ff.loc[['A', 'B']])
print (ff[['name','price']].loc[['A', 'B']])

# iloc is index based
# iloc[col, row]
print (ff.iloc[0:2])
print (ff.iloc[0:2, 1:3])
#    price  quantity
# A     10        90
# B     12        87

# select by condition
print (ff.price > 20)
print (ff[ff.price > 20])
#   name  price  quantity
# D    D     30        45
# A    A     40        20

print (ff.sort_values(by='price', ascending=False))

# Statistics
f2 = ff.filter(items=['price', 'quantity'])
print (f2)

print (f2.mean())
print (f2.std())
print (f2.describe())
#          price  quantity
# count   5.000000   5.00000
# mean   22.400000  53.00000
# std    12.601587  33.83046
# min    10.000000  20.00000
# 25%    12.000000  23.00000
# 50%    20.000000  45.00000
# 75%    30.000000  87.00000
# max    40.000000  90.00000