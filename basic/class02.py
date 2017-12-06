# __privateAttr

class People:
    def __init__(self, ID):
        self.__ssn = ID # private attr
        self.ssn = ID # nonprivate attr
        
    def printSSN(self):
        print (self.__ssn)
        
p = People('s01')
print (p.ssn)
p.printSSN()
# print (p.__ssn) # ERROR        