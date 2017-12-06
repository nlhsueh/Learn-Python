# LIST and FOR

# for loop (not the recommended style)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i].upper())

# for loop (recommended style)
for fruit in fruits:
    print(fruit.upper())

# use enumerate if you need to access the index
for index, fruit in enumerate(fruits):
    print(index, fruit)

# break
for fruit in fruits:
    if fruit == 'banana':
        print('Found the banana!')
        break # exit the loop and skip the 'else' block
else:
    print("Can't find the banana")

# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num**3) # [1, 8, 27, 64, 125]

# equivalent list comprehension
cubes = [num**3 for num in nums] # [1, 8, 27, 64, 125]

# for loop to create a list of cubes of even numbers
cubes2 = []
for num in nums:
    if num % 2 == 0:
        cubes2.append(num**3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes2 = [num**3 for num in nums if num % 2 == 0]    # [8, 64]

# for loop to cube even numbers and square odd numbers
cubes3 = []
for num in nums:
    if num % 2 == 0:
        cubes3.append(num**3)
    else:
        cubes3.append(num**2)

# equivalent list comprehension (using a ternary expression)
# syntax: [true condition if condition else false condition for variable in iterable]
cubes3 = [num**3 if num % 2 == 0 else num**2 for num in nums] # [1, 8, 9, 64, 25]

# for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)

# equivalent list comprehension
items = [item for row in matrix for item in row]

# set/list comprehension
fruits = ['apple', 'banana', 'cherry']
len_set = {len(fruit) for fruit in fruits}   # {5, 6}
len_list = [len(fruit) for fruit in fruits]