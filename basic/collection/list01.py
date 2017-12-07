# LISTS 

# create an empty list (two ways)
empty_list = []
empty_list = list()

students = ['nick', 'albert', 'jie']
age =[12, 56, 40]

# examine a list
students[0]
len(students) #length (count) of a list
max(age)
min(age)
['Python'] * 3 
'nick' in students
for a in age:
   print (a)

# list slicing [start:end:step]
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
weekdays[0]
weekdays[0:3] # mon, tues, wed
weekdays[:3]     
weekdays[3:] # thurs, fri
weekdays[-1] # fri
weekdays[::2] # step = 2  
weekdays[::-1] # reverse

# modify a list (does not return the list)
students.append('lisa') # append an element
students.extend(['nick', 'allen']) # extend a list
students.insert(0, 'maggie')           
students.remove('nick') # remove fist nick
students.pop(2) # remove and return                       
del students[0]
students[0] = 'peter'

# find elements in a list
students.count('nick')
students.index('albert')

# sort a list (modify the original list)
students.sort()
students.sort(reverse=True) # sort in reverse
students.sort(key=len) # sort by the key (len(str))

# concatenate lists (slower than 'extend' method)
members = students + ['ned', 'rod', 'todd']

# alternative method for returning the list backwards
list(reversed(weekdays))

# using lambda
grade = [[100,98,88,20], [67,78,89], [34,45,56]]
g = sorted(grade, key=lambda x: sum(x)) # sort by the sum

# return a sorted list (does not modify the original list)
s2 = sorted(grade)
s2 = sorted(grade, reverse=True)
s2 = sorted(grade, key=len)

# insert into an already sorted list, and keep it sorted
num = [10, 20, 40, 50]
from bisect import insort
insort(num, 30)

# create a second reference to the same list
num2 = num
num2[0] = 0 # modifies both 

# copy a list (three ways)
num_copy1 = num[:]
num_copy2 = list(num)
num_copy3 = num.copy()

# examine objects
num is num2 # True; same object
num is num_copy1 # False
num == num2 # True
num == num_copy1 # True; same content