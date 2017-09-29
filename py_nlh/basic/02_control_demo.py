"""
TOPIC 2: 控制（Control）
"""

age = int(input("Please enter an age: "))

if age <0:
    print ("Error")
elif age < 20:
    print ("Young man")
elif age < 50:
    print ("Strong man")
else: 
    print ("Wisdom man")
        
age = int(input("Please enter an age: "))
if (age <0): print ("Error")

age = int(input("Please enter an age: "))
if (age <0): 
    print ("Error") # Error code, 必須要內縮

names = ['nick', 'john', 'albert']
grade = [100, 99, 98]

for n in names:
    print (n, len(n))

# range

for i in range(4):
    print (i)    

for i in range(2,5):
    print (i)    
    
for i in range(0,10,3): # range(開始, 結束, 差)
    print (i)    


# 印出 1-100 所有的質數

for n in range(1, 100):
    for d in range (2,n):
        if n % d == 0:
            print (n, "等於", d, "*", n//d)
            break
    else:
        print (n, "是質數")

# break 跳出迴圈        

# Exercise ==> 改善上面的程式，使之可以印出質數的個數