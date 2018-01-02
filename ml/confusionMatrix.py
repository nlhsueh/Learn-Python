from sklearn.metrics import confusion_matrix

predicted = [0,1,1,0,0] 
real =      [1,1,1,0,0]
cm = confusion_matrix(real, predicted)
print ('The confusion metrix is: \n', cm)
# [[2 0]
# [1 2]]

predicted = [1,1,1,1,0] 
real =      [1,1,1,0,0]
cm = confusion_matrix(real, predicted)
print ('The confusion metrix is: \n', cm)
# [[1 1]
# [0 3]]

tn, fp, fn, tp = confusion_matrix(real, predicted).ravel()
print (tn, fp, fn, tp)
# 1 1 0 3

predicted = [1,1,1,1] 
real =      [0,0,0,0]
cm = confusion_matrix(real, predicted)
print ('The confusion metrix is: \n', cm)

real = [2, 0, 2, 2, 0, 1]
predicted = [0, 0, 2, 2, 0, 2]
cm = confusion_matrix(real, predicted)
print ('The confusion metrix is: \n', cm)