# using CSV modules

import csv
def dataProcess():
    """
    read grade from csv file and package into a sorted list
    @return list of name, grade of each subject, average (sort by average)
    """
    # ID, eng, math, phy
    f = open('grade2.csv', 'r')    
    student = []
    grades=[]
    for student in csv.reader(f): # read one line
        sum = 0
        name = student[0]
        eng = int(student[1])
        math = int(student[2])
        phy = int(student[3])
        sum += eng + math + phy
        avg = round(float(sum)/3, 2)
        grades.append([name, [eng, math, phy], avg])

    f.close()
    # 依據平均做漸增排序
    sortedGrade = sorted(grades, key=lambda x: x[-1], reverse=True)    
    return sortedGrade

g = dataProcess()
for e in g:
    print (e)