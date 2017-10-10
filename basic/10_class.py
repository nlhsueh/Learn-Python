#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# class
#

class MyClass:
    "a demo class"
    count = 0
    __x = 100
    def __init__(self, x):
        self.__x += x;
        self.count += 1
        
#   ERROR
#   def increase():
#        x += 1
        
#    ERROR
#    def increase():
#        self.x += 1
        
    def increase(self):
        self.__x += 1
 
    def printX(self):
        print (self.__x)
        
            
class DerivedClass(MyClass):
    y=100

c = MyClass(100)
c.increase()
c.printX()
c2 = MyClass(200)
print (MyClass.count)

#
# docstring
#

print (MyClass.__doc__)
print (c.__doc__)


print (".__doc__:", MyClass.__doc__)
print (".__name__:", MyClass.__name__)
print (".__module__:", MyClass.__module__)
print (".__bases__:", MyClass.__bases__)
print (".__dict__:", MyClass.__dict__)

#
# inheritance
# 

d = DerivedClass(100)

print (isinstance(c, DerivedClass))
print (isinstance(d, DerivedClass))
