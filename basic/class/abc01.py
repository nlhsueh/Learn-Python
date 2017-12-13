# declare an abstract class (two ways)
import abc

class ClassName (metaclass = abc.ABCMeta):
    pass

class ClassName2 (abc.ABC): 
    pass

# EXAMPLE
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def screaming(self):
        pass

    @abc.abstractmethod
    def walk(self, x, y):
        print ("use two leg")

a = Animal() # ERROR
        
class Dog(Animal):
   pass

d = Dog() # ERROR

class Cat(Animal):
   def screaming(self):
      print ("meow")
      
   def walk(self, x,y):
      super().walk(x,y)
      print ("jump")
                       
c = Cat()
c.screaming()
c.walk(12,1)