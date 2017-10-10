#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# List
# 包含 append, extend, insert, index 等運用
#

g1 = [12,22,99]
g2 = [100,100]
g1.append(g2)
g1

g1.append(20)
print (g1)

g1 = [12,22,99]
g2 = [100,100]
g1.extend(g2)
print (g1)

g1 = [12,22,99]
g2 = [100,100]
g1.insert(1,g2)
print (g1)

g1.remove(99)
g1.remove(98) # value error

g1 = [12,22,99]
print (g1.index(99))

g1 = [99,100,10]
g1.sort()
print (g1)

grade = []
grade.append([1,2])
grade

grade = [[1,2],[2,3]]
grade.append([4,5])
grade

names = ['nick', 'apple', 'john']
print (names.index('apple'))
names.sort()
names


# 更方便的設定 list 的值
s = [x**2 for x in range(10)]

s=[]
for x in range(10):
   s.append(x**2) 
   
s2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (s2)

#
# load csv file into grade
#

grade = []
import csv
f = open('grade.csv', 'r')
for row in csv.reader(f):
    print (row)
    g = []
    for d in row:
        g.append(int(d))
    grade.append(g)    
f.close()

print(grade)

# 直接放到 list 中：
grade = []
import csv
f = open('grade.csv', 'r')
grade_str = list(csv.reader(f))
print(grade_str)

grade=[]
for s in grade_str:
    # map(int, list): 可以把 list 內的 str 都轉為 int
    grade.append(list(map(int, s)))


# sort
    
grade = [[1,12,23], [67,78,89], [34,45,56]]

sorted(grade, key=lambda x: x[0])
grade