matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# append
matrix += [[13, 14, 15]]
# or matrix.append([16, 17, 18])

# add a 'column'
for index, element in enumerate([3, 6, 9, 12, 15]):
    matrix[index].append(element)

# Result: [[1, 2, 3, 3], [4, 5, 6, 6], [7, 8, 9, 9], [10, 11, 12, 12], [13, 14, 15, 15]]    