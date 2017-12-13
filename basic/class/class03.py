class People:
    def __init__(self, ID):
        self.__ssn = ID # private attr
        self.ssn = ID # nonprivate attr
                
    def __str__(self):
        return "SSN: " + self.__ssn
        
    def __repr__(self):  
        return "The SSN is " + self.__ssn
    

p = People('abc')    
print (p)
print (repr(p))