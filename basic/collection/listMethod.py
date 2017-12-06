#
# List method
#

x=[1,2]
y=[3,4]
x.append(y) # [1,2,[3,4]]

x.extend(y) # [1,2,3,4]

# insert: 放到特定位置
x.insert(100, y)
x
# remove: 移除某元素
List.remove(x)

# index: 找到第一個該值的位置
List.index(x)

# count(): 計算數量
a = [23, 23, 34, 45, 56, 45, 'FCU'] 	
print (a.count(23), a.count(34), a.count('t')) # 2 1 0 	

# reverse(): 從後面數
a.reverse() # ['FCU', 45, 56, 45, 34, 23, 23]

# sort(): 排序
a.sort() # [23, 23, 34, 45, 45, 56 , 'FCU'] 

# 當成 Stack 用
stack = [3, 4, 5]
stack.append(6) # Stack is now [3, 4, 5, 6]

item = stack.pop() 
item # 6 
stack # [3, 4, 5] 