from sklearn import preprocessing
import pandas as pd

# employee's city, age and ID
X = pd.DataFrame([["Taipei", 23, 1], ["Taichung", 32, 2], ["Tainan",12, 3], ["Kaosiuang", 44, 4]])

X = X.iloc[:, 0:2].values # we don't need the ID field
print (X)

# LABEL ENCODER
encoder = preprocessing.LabelEncoder()
X[:, 0] = encoder.fit_transform(X[:, 0]) # encode the city field
print (encoder.classes_)
# ['Kaosiuang' 'Taichung' 'Tainan' 'Taipei']

print (X)
# [[3 23]
#  [1 32]
#  [2 12]
#  [0 44]]

# ONE HOT ENCODER
onehotencoder = preprocessing.OneHotEncoder(categorical_features = [0])

X = onehotencoder.fit_transform(X).toarray()
print (X)
# [[  0.   0.   0.   1.  23.]
#  [  0.   1.   0.   0.  32.]
#  [  0.   0.   1.   0.  12.]
#  [  1.   0.   0.   0.  44.]]

# Avoiding the Dummy Variable Trap
X = X[:, 1:]
print (X)
# [[  0.   0.   1.  23.]
#  [  1.   0.   0.  32.]
#  [  0.   1.   0.  12.]
#  [  0.   0.   0.  44.]]