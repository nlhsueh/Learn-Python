"""
String
"""

food = 'egg'
food

food = "egg"
food

for s in food:
    print (s)
    
template = "I was %d years old, born at %s"
Nick = template % (17, "Taichung")    
Nick
    
# Using control code \

# 'doesn't' # error code => error
'doesn\'t'
"This \"concept\" is important"
# print () will produce a readable output
print('"Isn\'t," she said.')

# r: raw, 用來取消控制碼 \
print(r'C:\some\name') 
text = ('今天要來說一個很長的故事'
        '從前有一個國王，有一對兒女...')
text[0]
text[1:3]
len(text) # len 可以傳回該字串的長度

"""
time
"""
import time
time.time()
time.localtime()
time.asctime()
time.asctime(time.localtime())
time.sleep(3)

import calendar
cal = calendar.month(2018,1)
print (cal)

"""
datetime
"""
from datetime import date
d = date.today()
t = d.timetuple()
t
for x in t:
    print (x)

d.isoformat()

