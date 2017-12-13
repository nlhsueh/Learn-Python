# STATIC METHOD
class P:
    def prime(v):
        "列出 v 以下的所有質數" # docstring
        for n in range(2, v):
            for d in range (2,n):
                if n % d == 0:
                    print (n, "等於", d, "*", n//d)
                    break
            else:
                print (n, " 是質數")

P.prime(10)
#p = P()
#p.prime()