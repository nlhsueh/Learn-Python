# 
# GRADEBOOK example
#

grade = [100, 40, 19, 85, 75, 72]
grade[0]
grade[-1]
grade[:]
grade[1:4]
grade[:4]
grade[1:]
print(len(grade))

sum = 0
for g in grade:
    sum = sum + g
sum    

sum = 0
for g in grade:
    sum += g
sum    

grade + [0, 22] # 相當於 append
grade

grade[0] = 99
grade

grade = grade + [0, 22]
grade

grade.sort()
grade

letters = ['n','i','c','k']
letters

names = ['nick', 'john', 'albert']
names

# [12,1,100] English, Math, Physical grade fo student 0
t_grade = [[12,1,100], [34, 32, 72], [45,99,100]]

std1_grade = t_grade[0]
t_grade[0][1]

std1_grade

# average of student 1
sum = 0
for g in t_grade[0]:
    sum += g
print (round(sum/len(t_grade[0])))

# print each student's average grade
for student in t_grade:
    sum = 0
    for student_g in student:
        sum += student_g
    print(round(sum/len(student)))

# 二維的，可以存每個學生的每科成績
# !!! you can't get column element by this way!!! 
subject_grade = t_grade[:][0]    
subject_grade

# 建構 English 的 list
subject = []
for g in t_grade:
    subject.append(g[0])
print (subject)    

# 我們也可以寫成副程式，這樣就可以回傳每一個不同的科目
def getSubject(grade, i):
    subject = []
    for g in grade:
        subject.append(g[i])
    return subject 

t_grade = [[12,1,100], [34, 32,72], [45,99,100]]

Eng_list = getSubject(t_grade, 0)
Math_list = getSubject(t_grade, 1)
Phy_list = getSubject(t_grade, 2)
print (Eng_list)

subject_list = [Eng_list, Math_list, Phy_list]
print (subject_list)

subject_avg=[]
for subject in subject_list:
    print (subject)
    sum=0
    for g in subject:
        sum += g
    subject_avg.append(round(sum/len(subject)))

print(subject_avg)    


""" 
Exercise
* 寫一個副程式，將二維的 t_grade 的行列對調
* 例如 [[1,2,3],[4,5,6],[7,8,0]] => [[1,4,7],[2,5,8],[3,6,9]]
exchange(grade)
"""


# 
# EXERCISE 
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


# create a list of x-square: 0, 1, 4, ...
s = [x**2 for x in range(10)]

# another way
s=[]
for x in range(10):
   s.append(x**2) 

# combination in a condition    
s2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (s2)

#
# READ CSV to LIST
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