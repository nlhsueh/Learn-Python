from sklearn import preprocessing
import matplotlib.pyplot as plt

# EXAMPLE 1
data = [[100, 0], [100, 0], [0, 1], [0, 1]]
scaler = preprocessing.StandardScaler()
print(scaler.fit(data))
print(scaler.mean_)
d2 = scaler.transform(data)
print(d2)
print(scaler.transform([[199, 2]]))

# EXAMPLE2
from sklearn.datasets.samples_generator import make_classification

X, y = make_classification(n_samples=300, n_features=2 , 
                           n_redundant=0, n_informative=2,random_state=22, 
                           n_clusters_per_class=1, scale=(10, 100))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(X[:, 0], X[:, 1], c=y)
#plt.show()

X = preprocessing.scale(X)
plt.subplot(1,2,2)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.savefig('images/scale.png')
#plt.show()