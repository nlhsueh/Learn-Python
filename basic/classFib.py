class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        print ("a")
        return self

    def __next__(self): # 宣告 Fib 是一個 iterator
        fib = self.a
        if fib > self.max:
            raise StopIteration # StopIteration 並不是例外
        self.a, self.b = self.b, self.a + self.b
        return fib  
    
for n in Fib(1000):
    print (n, end=' ')