# LIST OF LIST

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# examine a list
matrix[2]           
matrix[2][0]

# enumerate
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print ('matrix', i, j, '=', element)

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print (matrix[row][column], end=' ')
    print ("\n")    

# append
matrix += [[13, 14, 15]]

# add a 'column'
for index, element in enumerate([3, 6, 9, 12, 15]):
    matrix[index].append(element)