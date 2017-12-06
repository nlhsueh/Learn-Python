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
        birth_year = 2017-self.age # local variable
        print ('birth year: ', birth_year)
        
c = People(20)
d = People(20)
c.increase()
c.printAge()   

print ('Count of people: ', People.count, c.count, d.count)
print ('Show instance var: ', c.age, d.age)
print (People.__doc__)
print (hasattr(c, 'age'))