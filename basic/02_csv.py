#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    csv demo
"""

import csv

def dataProcess():
    # 學校, eng, math, phy 的成績    
    f = open('grade2.csv', 'r')
    
    student = []
    grades=[]
    for student in csv.reader(f):
        sum = 0
        name = student[0]
        eng = int(student[1])
        math = int(student[2])
        phy = int(student[3])
        sum += eng + math + phy
        avg = round(float(sum)/3, 2)
        grades.append([name, [eng, math, phy], avg])
    sortedGrade = sorted(grades, key=lambda x: x[-1], reverse=True)    
    # 依據平均做漸增排序
    f.close()
    return sortedGrade

g = dataProcess()
print (g)