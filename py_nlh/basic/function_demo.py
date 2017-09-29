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