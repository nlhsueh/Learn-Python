
# load file into grade
"""
load CSV into list
"""
import csv
import numpy as np
import math    
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False #表示負號

"""
回傳 課程名稱, 修課人數, 登入次數, 每人平均登入次數
"""
def dataProcess():
    # 每門課的名稱，選課人數，觀看次數，作答次數，登入次數等資訊    
    f = open('hot.csv', 'r',  encoding='utf-8')
    
    course = []
    Q=[]
    header=True
    for course in csv.reader(f):
        if not header: 
            name = course[1]
            count = int(course[2]) # 平均每人登入次數
            login = int(course[7])
            if count == 0:
                continue
            else:
                avg = round(float(login)/count, 2)
                Q.append([name[:4], count,login,avg])
        header = False
    sortedQ = sorted(Q, key=lambda x: x[-1], reverse=True)    
    QQ = np.array(sortedQ)
    return QQ

"""
回傳 list, 紀錄此筆資料的 max, min, avg, std
* 跳過資料為 -1 (無意義資料)
"""
def info(data):
    sum = 0
    max = data[0]
    min = data[0]
    for d in data:
        sum += d
        if d > max:
            max = d
        if d < min:
            min = d
    data_len = len(data)
    avg = round(float(sum)/data_len,2)
    sum2 = 0
    for d in data:
        d = float(d)
        sum2 += (d-avg)*((d-avg))
    std = math.sqrt(sum2/data_len)
    mean = data[data_len//2]
    return (max, min, mean, avg, std)

"""
Using numpy function to get statistic data
"""
def info2(data):
    max = data.max()
    min = data.min()
    mean = data.mean()
    avg = np.average(data)
    std = data.std()
    return (max, min, mean, avg, std)

# remove the courses that registers over 1500
def removeOutlier(X, Y):
    idx=0
    for i in X:
        if i > 1500:
            X = np.delete(X, idx, 0)
            Y = np.delete(Y, idx, 0)
        idx += 1
    return (X, Y)    

def showDistribution(h):
#    import numpy as np
    import scipy.stats as stats
    import pylab as pl
    fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
    pl.xlabel('平均每人登入次數')
    pl.ylabel('比率')    
    pl.plot(h,fit,'-o')
    pl.hist(h,normed=True)      #use this to draw histogram of your data
    pl.show()    

def showHistgram(d):
    import scipy.stats as stats
    import pylab as pl
    pl.plot(d)
    pl.show()    

def norm(d):
    norm=np.linalg.norm(d)
    if norm==0: 
       return d
    return d/norm
    
# print basic data        
hotList = dataProcess()

print ("---- Hot list ----")
print (hotList)

# print basic statistic data
rateList = hotList[:,-1].astype(float) #每課程中平均每人登入次數
template = "平均每人登入次數：Max is %.2f, min is %.2f, mean is %.2f, average is %.2f, std is %.2f"
d = info(rateList)
max, min, mean, avg, std = info(rateList)
print (template % (max, min, mean, avg, std))

print (template %  info2(rateList))

# show distribution
X = hotList[:,1].astype(np.int) # 修課人數
Y = hotList[:,2].astype(np.int) # 登入次數

X, Y = removeOutlier(X, Y)

z = Y/X
z = z/np.max(z) * 100

showHistgram(z)

print (template %  info2(z))

showDistribution(z)

# scatter graph

plt.scatter(X, Y, color = 'red')
#plt.plot(X, Y, color = 'blue')
#plt.title('Salary vs Experience (Training set)')
plt.xlabel('註冊人數')
plt.ylabel('登入次數')
plt.show()
 
dd = np.random.randn(10)