#
# DICTIONARIES 
# properties: unordered, iterable, mutable, can contain multiple data types
# made of key-value pairs
# keys must be unique, and can be strings, numbers, or tuples
# values can be any type
#

# Create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()

# Create a dictionary (two ways)
family = {'dad':'Homer', 'mom':'Marge', 'size':6}
family = dict(dad='Homer', mom='Marge', size=6)

# Convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'Homer'), ('mom', 'Marge'), ('size', 6)]
family = dict(list_of_tuples)

# Examine a dictionary
family['dad']       # returns 'Homer'
len(family)         # returns 3
'mom' in family     # returns True
'marge' in family   # returns False (only checks keys)

# Returns an iterable view (Python 3)
family.keys()       # keys: ['dad', 'mom', 'size']
family.values()     # values: ['Homer', 'Marge', 6]
family.items()      # key-value pairs: [('dad', 'Homer'), ('mom', 'Marge'), ('size', 6)]

# Modify a dictionary (does not return the dictionary)
family['cat'] = 'snowball'              # add a new entry
family['cat'] = 'snowball ii'           # edit an existing entry
del family['cat']                       # delete an entry
family['kids'] = ['bart', 'lisa']       # dictionary value can be a list
family.pop('dad')                       # remove an entry and return the value ('homer')
family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries

# Access values more safely with 'get'
family['mom']                       # returns 'Marge'
family.get('mom')                   # equivalent
family['grandma']                   # throws an error since the key does not exist
family.get('grandma')               # returns None instead
family.get('grandma', 'not found')  # returns 'not found' (the default)
'Homer' in family					# True

# Access a list element within a dictionary
family['kids'][0]                   # returns 'bart'
family['kids'].remove('lisa')       # removes 'lisa'

# String substitution using a dictionary
'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'

# Iterate through two things at once (using tuple unpacking)
family = {'dad':'Homer', 'mom':'Marge', 'size':6}
for key, value in family.items():
    print(key, value)

# Dictionary comprehension
fruits = ['apple', 'banna', 'cherry']
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              
# {'apple': 5, 'banana': 5, 'cherry': 6}
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} 
# {'apple': 0, 'banana': 1, 'cherry': 2}

# Sort
s2 = sorted(gradebook.keys())