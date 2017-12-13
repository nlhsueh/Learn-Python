# __privateAttr

class People:
    def __init__(self, ID):
        self.__ssn = ID # private attr
        self._ssn = ID # protected attr
        self.ssn = ID # nonprivate attr
        
    def printSSN(self):
        print (self.__ssn)
        
p = People('s01')
print (p.ssn)
print (p._ssn) # ok but not recommended
print (p.__ssn) # ERROR        
p.printSSN()