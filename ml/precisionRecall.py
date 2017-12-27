from sklearn.metrics import precision_recall_fscore_support as score
import numpy as np

def printMetrics(real, predicted):
    precision, recall, fscore, support = score(real, predicted)

    print ('pre: ', precision)
    print ('rec: ', recall)
    print ('f  : ', fscore)
    print ('sup: ', support)

np.set_printoptions(precision=2)

# 謹慎判斷 1
predicted = [0,1,1,0,0] 
real =      [1,1,1,0,0]
printMetrics(real, predicted)

# 對 1 寬鬆
predicted = [1,1,1,1,0] 
real =      [1,1,1,0,0]
printMetrics(real, predicted)

predicted = [1,1,1,1] 
real =      [0,0,0,0]
printMetrics(real, predicted)

predicted = [1,2,3,4,5,1,2,1,1,4,4] 
real =      [1,2,3,4,4,1,2,1,1,4,1]
printMetrics(real, predicted)

