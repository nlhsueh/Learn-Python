#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:12:03 2017

@author: nlhsueh
"""

class C:
    __x=100
    y=50        
    def inc(self):
        self.__x += 1
        C.__x += 100        
    def print(self):
        print ("C.__x", C.__x)        
        print ("self.__x", self.__x)
c1 = C()
c1.inc()
c1.print()

c2 = C()
c2.inc()
c2.print()
