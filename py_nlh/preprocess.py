# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
"""
不同國家、年齡、薪水的是否會購買
* dependent: purchase
"""
dataset = pd.read_csv('Purchase.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
"""
* NaN: not a number
* 採用 mean 的方式來填補資料
* 填補 第一欄（age）、第二欄(salary)的資料
"""
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print (X)

# Encoding categorical data
# Encoding the Independent Variable
"""
* 把第0欄 (country) 的資料 transform
"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
print (X)

"""
one hot encoder
"""
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
print (y)