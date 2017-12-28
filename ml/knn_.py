import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
print (iris)

print (len(iris_data))

# show some data and label
print(iris_data[0], iris_data[79], iris_data[100])
print(iris_labels[0], iris_labels[79], iris_labels[100])

np.random.seed(42)
indices = np.random.permutation(len(iris_data))
print (indices)

n = 12 # number of test
X = iris_data[indices[:-n]] # training data set

y = iris_labels[indices[:-n]] # training data label
T = iris_data[indices[-n:]] # testing data set
t = iris_labels[indices[-n:]] # testing data lebel

print(X[:4], y[:4])
print(X[:4], y[:4])

def distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)
    # Euclidean Distance

print(distance(X[3], X[44])) # a test

def get_neighbors(X, 
                  y, 
                  test_instance, 
                  k, 
                  distance = distance):
    """
    計算與 'test_instance' 最近的 k 個鄰居
    回傳鄰居包含三個資料：(index, dist, label)，依據 dist 作由小到大的排序
    index    is the index from the training_set, 
    dist     is the distance between the test_instance and the 
             instance training_set[index]
    distance is a reference to a function used to calculate the 
             distances
    """
#    You code here
#    
#    
#    
#    
    neighbors = distances[:k]
    return neighbors

"""
VOTE the MOST COMMON
"""        
from collections import Counter
def vote(neighbors):
    '''
    計算 k 鄰居都在哪一類 (label)，和最多的同一類
    '''
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1 #neightbor[2] is the label
    print (class_counter)    
    return class_counter.most_common(1)[0][0]
        # most common: 最多的
        # (1): 只找一個

for i in range(5):
    neighbors = get_neighbors(X, 
                              y, 
                              T[i], 
                              2, 
                              distance=distance)
    
    print("index: ", i, 
          ", result of vote: ", vote(neighbors), 
          ", label: ", y[i], 
          ", data: ", X[i])
    
"""
VOTE PROPABILITY
"""        
def vote_prob(neighbors):
    '''
    附上歸為該 label 的機率
    '''
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    return winner, votes4winner/sum(votes)

# show someone's neigbors
for i in range(n):
    neighbors = get_neighbors(X, 
                              y, 
                              T[i], 
                              5, 
                              distance=distance)
    print("index: ", i, 
          ", vote_prob: ", vote_prob(neighbors), 
          ", label: ", y[i], 
          ", data: ", X[i])  