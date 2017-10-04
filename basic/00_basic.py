#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:31:09 2017

@author: nlhsueh
"""

name = input("You name? ")
print (name)
age = int(input("Your age? "))
if age < 20:
   print (name, ", You are so young")



x = 100; grade = [12, 45, 90]
x in grade
x not in grade


"""
Identity operator
"""
a = [1,2,3]
b = [1,2,3]
a is b

c = a
c is a