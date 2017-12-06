#
# DEFINING FUNCTIONS 
#

# define a function with no arguments and no return values
def print_text():
    print('this is text')

# call the function
print_text()

# define a function with one argument and no return values
def print_this(x):
    print(x)

# call the function
print_this(3)       # prints 3
n = print_this(3)   # prints 3, but doesn't assign 3 to n
                    #   because the function has no return statement

# define a function with one argument and one return value
def square_this(x):
    return x**2

# include an optional docstring to describe the effect of a function
def square_this(x):
    """Return the square of a number."""
    return x**2

# call the function
square_this(3)          # prints 9
var = square_this(3)    # assigns 9 to var, but does not print 9

# define a function with two 'positional arguments' (no default values) and
# one 'keyword argument' (has a default value)
def calc(a, b, op='add'):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    else:
        print('valid operations are add and sub')

# call the function
calc(10, 4, op='add')   # returns 14
calc(10, 4, 'add')      # also returns 14: unnamed arguments are inferred by position
calc(10, 4)             # also returns 14: default for 'op' is 'add'
calc(10, 4, 'sub')      # returns 6
calc(10, 4, 'div')      # prints 'valid operations are add and sub'

# ** keyword argument
def score(name, **grade):
    print ('The grade of', name)
    for e in grade.items:
        print (e)

score ('nick', eng='90', math='100', phy='99')        

# use 'pass' as a placeholder if you haven't written the function body
def stub():
    pass

# return two values from a single function
def min_max(nums):
    return min(nums), max(nums)

# return values can be assigned to a single variable as a tuple
nums = [1, 2, 3]
d = min_max(nums)                   # (1, 3)

# return values can be assigned into multiple variables using tuple unpacking
x, y = min_max(nums)                # x = 1, y = 3

# variable-length argument
def get_min(*data):
   sum = 0
   m = data[0]
   for d in data:
      if d < m:
        m = d
   return m

print (get_min(1,2))       
print (get_min(12,1,99,-1)) 


a = avg ('nick', 100, 50, 20)
print (a)

b = avg('taylor', 100, 50, 20,90)
print (b)


#
# ANONYMOUS (LAMBDA) FUNCTIONS 
# primarily used to temporarily define a function for use by another function
#

# define a function the "usual" way
def squared(x):
    return x**2

# define an identical function using lambda
squared = lambda x: x**2

# sort a list of strings by the last letter (without using lambda)
simpsons = ['homer', 'marge', 'bart']
def last_letter(word):
    return word[-1]
sorted(simpsons, key=last_letter)

# sort a list of strings by the last letter (using lambda)
sorted(simpsons, key=lambda word: word[-1])

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
print (pairs)
pairs.sort()
print (pairs)

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key = lamda pair: pair[1])
print (pairs)

# EXAMPLE: prime

def print_prime(v):
    for n in range(1, v):
        for d in range (2,n):
            if n % d == 0:
                print (n, "等於", d, "*", n//d)
                break
        else:
            print (n, "是質數")

print_prime(20)         


# return

def get_prime(v):
    prime = []
    for n in range(1, v):
        for d in range (2,n):
            if n % d == 0:
                print (n, "等於", d, "*", n//d)
                break
        else:
            prime.append(n)
            print (n, "是質數")
    return prime

p = get_prime(20)


def get_prime(v, start=1):
    prime = []
    for n in range(start, v):
        for d in range (2,n):
            if n % d == 0:
                print (n, "等於", d, "*", n//d)
                break
        else:
            prime.append(n)
            print (n, "是質數")
    return prime

get_prime(100,start=50) # keyword argument
get_prime(100,50)

get_prime(start=50) # Error


# 必要參數一定要放前面，且一定要被設定 
# def get_prime(start=1, v): ... is a Error definition

def get_prime(start=1, v=10):
    prime = []
    for n in range(start, v):
        for d in range (2,n):
            if n % d == 0:
                print (n, "等於", d, "*", n//d)
                break
        else:
            prime.append(n)
            print (n, "是質數")
    return prime

get_prime(100,start=50) # keyword argument
get_prime(100,50)

# copy and pass
def avg(name, grade):
   sum = 0
   grade.extend([100,100])
   for g in grade:       
      sum += g
   avg = sum//len(grade)   
   print (name + " 的平均是：", avg)   

g = [20,20]
a = avg ('nick', g)
print (g)

g = [20,20]
a = avg ('nick', g.copy())
print (g)
