import pandas as pd

ff = pd.read_csv("fruitTitle.csv", 
                  header=0,
                  names=["name", "price", "quantity"],
                  index_col=0,
                  sep=",", 
#                  thousands=","
                  )
print(ff)
print (ff.columns)
ff.describe()

# Statistics
f2 = ff.filter(items=['price', 'quantity'])
print (f2)

print (f2.mean())
print (f2.std())
print (f2.describe())
