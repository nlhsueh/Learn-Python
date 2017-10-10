#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:28:15 2017

@author: nlhsueh
"""

import numpy as np
c = np.arange(27).reshape(3,3,3) 
print (c)

print (c[0])

a = np.array([1234])

a = np.array([[1112131415], [1617181920212223242526272829303132333435]])

print (a)

a = np.arange(16).reshape(4,4)
print (a[:2, :2])
print (a[:2, :])

print (a[::2, :])

print (a[:, 1:3])
