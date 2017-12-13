# CLASS VAR and INSTANCE VAR

class People:    
    """
    A class to describe a person
    """
    count = 0 # class variable
    def __init__(self, age):    
        self.age = age # age is instance variable
        People.count += 1 # access class variable
                
    def increase(self):
        self.age += 1
 
    def printAge(self):
        print ('age: ', self.age)
        birth_year = 2017 - self.age # local variable
        print ('birth year: ', birth_year)
        
c = People(20)
d = People(20)
c.increase()
c.printAge()   

print ('Count of people: ', People.count, c.count, d.count)
print ('Show instance var: ', c.age, d.age)

# BUILT IN ATTRIBUTES
print (People.__doc__)
print (People.__dict__)
print (People.__module__)
print (People.__bases__)
print (hasattr(c, 'age'))

class P(People):
    pass

print (P.__bases__) # (<class '__main__.People'>,)

# FUNCTIONS
hasattr(c, 'age')
hasattr(c, 'tall')
getattr(c, 'age')
setattr(c, 'age', 25)
print (c.age) # 25
delattr(c, 'age')
hasattr(c, 'age')

# ADDING ATTRIBUTES

class Employee:
    pass

e = Employee()
e.age = 12
e.name = 'nick'

e2 = Employee()
e2.name = 'john'
e2.age = 54

print (e.name, e.age)
print (e2.name, e2.age)
