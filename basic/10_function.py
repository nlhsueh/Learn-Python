# Define function

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

p

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


# variable-length argument

def avg(name, *grade):
   sum = 0
   for g in grade:
      sum += g
   avg = sum//len(grade)   
   print (name + " 的平均是：", avg)   

a = avg ('nick', 100, 50, 20)
print (a)

b = avg('taylor', 100, 50, 20,90)
print (b)


# lambda

avg = lambda eng, math, phy: round((eng+math+phy)/3,2)

a = avg (12,23,34) # 呼叫端


# call by reference

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


# pass int

def add(x, y):
    r = x + y
    x += 10
    y += 10
    return (r)

x1 = y1 = 100
print (x1, y1)

def hello(name):
    name = "hello " + name
    print (name)

n = "nick"
hello(n)
print (n)

# lamda

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
print (pairs)
pairs.sort()
print (pairs)

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key = lamda pair: pair[1])
print (pairs)



