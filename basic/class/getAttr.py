# I: using getattr
class People:
    def __init__(self, birth_year):
        self.year = birth_year
     
    def __getattr__(self, key):
        if key == 'age':
            return 2017 - self.year
        else:
            raise AttributeError
    
p = People(2000)   
print (p.age)
p.age = 50
print (p.age)

# II: using getattribute
class People2:
    def __init__(self, birth_year):
        self.year = birth_year
        self.age = 100
     
    def __getattribute__(self, key):
        if key == 'age':
            return 2017 - self.year
        else:
            raise AttributeError
    
p = People2(2000)   
print (p.age)
p.age = 50
print (p.age)