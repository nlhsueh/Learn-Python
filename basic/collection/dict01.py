# DICTIONARY

# create an empty dictionary
empty_dict = {}
empty_dict = dict()

# create a dictionary (two ways)
family = {'dad':'Homer', 'mom':'Marge', 'size':6} # {key:value}
family = dict(dad='Homer', mom='Marge', size=6) # dict(key=value)

# key 可以是 int, string, tuple 等不可修改的形態
grade = {1:12, 2:100, 3:90}

# key 的形態必須 immutable, List 是不行的：
grade = {'[eng]':12, 'math':100, 'phy':90, 'eng':90} # ERROR!

# convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'Homer'), ('mom', 'Marge'), ('size', 6)]
family = dict(list_of_tuples)

# examine a dictionary
family['dad']       # returns 'Homer'
len(family)         # returns 3
'mom' in family     # returns True
'marge' in family   # returns False (only checks keys)

# returns an iterable view (Python 3)
family.keys()       # keys: ['dad', 'mom', 'size']
family.values()     # values: ['Homer', 'Marge', 6]
family.items()      # key-value pairs: [('dad', 'Homer'), ('mom', 'Marge'), ('size', 6)]

# modify/add a dictionary (does not return the dictionary)
family['cat'] = 'snowball'              # add a new entry
family['cat'] = 'snowball ii'           # edit an existing entry
family['baby'] = 'maggie'
del family['cat']                       # delete an entry
family['kids'] = ['bart', 'lisa']       # dictionary value can be a list
family.pop('dad')                       # remove an entry and return the value ('homer')
family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries

# access values more safely with 'get'
family['mom']                       # returns 'Marge'
family.get('mom')                   # equivalent
family['grandma']                   # throws an ERROR since the key does not exist
family.get('grandma')               # returns None instead
family.get('grandma', 'not found')  # returns 'not found' (the default)
'Homer' in family					# True

# access a list element within a dictionary
family['kids'][0]                   # returns 'bart'
family['kids'].remove('lisa')       # removes 'lisa'

# string substitution using a dictionary
'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'

# iterate through two things at once (using tuple unpacking)
family = {'dad':'Homer', 'mom':'Marge', 'size':6}
for key, value in family.items():
    print(key, value)

# dictionary comprehension
fruits = ['apple', 'banna', 'cherry']
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              
# {'apple': 5, 'banana': 5, 'cherry': 6}
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} 
# {'apple': 0, 'banana': 1, 'cherry': 2}

# sort: you can't sort the dict
gradebook = {'Zen':100,'Alen':90,'Peter':20,'Mary':56}
s2 = sorted(gradebook.keys())
for name in s2:
    print (name, gradebook[name])