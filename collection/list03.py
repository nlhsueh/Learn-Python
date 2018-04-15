# LIST OF LIST

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# examine a list
matrix[2]           
matrix[2][0]

for row in matrix:
    for element in row:
        print (element, end=' ')
    print ()

# enumerate
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print ('M[{},{}]={}'.format(i,j,element))
        
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print ('M[{},{}]={}'.format(row,col,matrix[row][col]))