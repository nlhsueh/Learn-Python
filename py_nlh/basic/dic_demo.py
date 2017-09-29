"""
Tuple
* Sequence types: set, tuple, and range
* tuple = (,,,)
* tuple is immutable
"""

s= 1,2,3
print (s[0])
1 in s
s[0]=100  # Error


"""
Dictionary
* key:value 所構成的資料群
* key 必須是不可修改的（string, number, tuples）
"""

g = {1:100, 2:98, 3:88}
g[1]

gradebook= {'nick':100, 'albert':98, 'peter':97}
print (gradebook['nick'])

del gradebook['peter']
gradebook['nick'] = 99

list(gradebook.keys())
list(gradebook.values())
'nick' in gradebook

gbook = {'nick':100, 'nick':98} # 錯誤！key 必須惟一

# 使用 dict constructor
gradebook = dict(nick=100, albert=99, peter=98)
gradebook

sorted(gradebook.keys())

for (k,v) in gradebook.items():
    print (k,v)

type(gradebook.items())

"""
enumerate(sequence)
* 回傳一個 enumerate 物件，會在前面加上序號
"""

set_gb = [12,99,100]
dict_gb = {'nick':12, 'albert':100, 'peter':99}
tuple_gb = (12, 99, 100)

print (type(enumerate(set_gb)))

for (i, v) in enumerate(set_gb):
    print (i, v)
for (i, v) in enumerate(dict_gb):
    print (i, v)
for (i, v) in enumerate(tuple_gb):
    print (i, v)
    
s=list(enumerate(set_gb))
s    

a = 200
print (a)