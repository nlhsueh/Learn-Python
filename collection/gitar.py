
s=[]
for i in range(1,51):
    s.append('s'+str(i))

gt = set([])
cs = set([])

import random
while len(gt) < 10:
    i = random.randint(0, 49)
    gt.add(s[i])

print ("吉他: ", gt)    
        
while len(cs) < 10:
    i = random.randint(0, 49)
    cs.add(s[i])

print ("電腦: ", cs)
    
print ("電腦與吉他: ", cs & gt)    
    