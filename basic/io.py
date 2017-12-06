# String = input(String)

name = input("You name? ")
print (name)

age = int(input("Your age? "))

# print using %
print ('hello %s, you are %d' % (name, age))
print ('hello, ', name, 'you are ', age)

# new way of formating: string.format()
print ('hello, {0} you are {1}'.format(name, str(age)))
   # {0} refers to name
   # {1} refers to str(age)

import math
print('The value of pi: {0:.3f}.'.format(math.pi))

table = {'Nick': 41, 'Alen': 3, 'Jack': 102}
for name, age in table.items():
    # the min space for name is 10
    print('{0:10} ==> {1:3d}'.format(name, age))
    
# open file
f = open('age.txt')
for line in f:
    print (line)
f.close()    

# using with open (..) ... as 
with open('age.txt') as f:
    read_data = f.read()
    print (read_data)
    print (f.mode)