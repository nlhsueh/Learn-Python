import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __call__(self, x, y): # object acts like a function
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    
    def __len__(self): # object acts like a set
        x = self.x
        y = self.y
        return int(math.sqrt(x*x + y*y))
    
    def __contains__(self, loc): # object acts like a set
        x = loc[0]
        y = loc[1]
        if self.x > x and self.y > y:
            return True
        return False

p = Location(12, 13);
print (p)

p(13, 14)
print (p)

print (len(p))
print ((1,1) in p)
print ((100,1) in p)