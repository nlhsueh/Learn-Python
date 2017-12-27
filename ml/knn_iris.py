#from __future__ import print_function
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print (iris_X[:2])
print(iris_y[:2])

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
# 0.3 for testing, 0.7 for training data

print(y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

predicted = knn.predict(X_test)
print('The prediction: ', predicted)
print('The real data: ', y_test)


