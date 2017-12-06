class Employee:
   def __init__(self, name, ID):
      self.name = name
      self.ID = ID
      
   def print(self):
       print (self.name, self.ID)

class Engineer(Employee): 
   def __init__ (self, name, ID, expert):
       # 呼叫父類別的建構子
       super(Engineer, self).__init__(name, ID)
       self.expert = expert

   # overriding       
   def print(self):
       print (self.name, self.ID, self.expert)
       
e = Employee('Jack', 's01')       
e.print()
print (isinstance(e, Employee))
print (isinstance(e, Engineer))
       
e2 = Engineer('Alen', 's02', 'Java')       
e2.print()       
print (isinstance(e2, Employee))
print (isinstance(e2, Engineer))       