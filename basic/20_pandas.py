#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# pandas application
#

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('grade2.csv')
print (dataset)

X = dataset.iloc[:, 2:4]
print (X)

Y = dataset.iloc[:, -1]
print (Y)