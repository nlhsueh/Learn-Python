matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# adding a row
matrix += [[13, 14, 15]]
# >> [[0, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

print (matrix)

# adding a column
for index, element in enumerate([3, 6, 9, 12, 15]):
    matrix[index].append(element)

print (matrix)