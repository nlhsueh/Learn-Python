#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:46:16 2017

@author: administrator
"""

class People:
    
    count = 0
    def __init__(self,age,tall):
        self.age = 10
        self.tall = 100
        
    def printAge(self):
        print (self.age)
        
    def counting(self):
        self.count += 1
        print (self.count)

x = People(12,182)
x.printAge
x.counting        
        
        
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)        