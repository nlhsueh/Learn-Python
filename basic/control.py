#
# COMPARISONS AND BOOLEAN OPERATIONS 
#

# assignment statement
x = 5

# comparisons (these return True)
x > 3
x >= 3
x != 3
x == 5

# boolean operations (these return True)
5 > 3 and 6 > 3
5 > 3 or 5 < 3
not False
False or not False and True     # evaluation order: not, and, or

#
# CONDITIONAL STATEMENTS 
#

# if statement
if x > 0:
    print('positive')

# if/else statement
if x > 0:
    print('positive')
else:
    print('zero or negative')

# if/elif/else statement
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')

# single-line if statement (sometimes discouraged)
if x > 0: print('positive')

# single-line if/else statement (sometimes discouraged)
# known as a 'ternary operator'
'positive' if x > 0 else 'zero or negative'

# EXERCISE: how old are you        

age = int(input("Please enter an age: "))

if age <0:
    print ("Error")
elif age < 20:
    print ("Young man")
elif age < 50:
    print ("Strong man")
else: 
    print ("Wisdom man")


#
# FOR
#

# range

for i in range(4):      # 0, 1, 2, 3
    print (i)    

for i in range(2,5):    # 2, 3, 4
    print (i)    
    
for i in range(0,10,3): # range(開始, 結束, 差)
    print (i)           # 0, 3, 6, 9



# BREAK
# 印出 1-100 所有的質數

for n in range(1, 100):
    for d in range (2,n):
        if n % d == 0:
            print (n, "等於", d, "*", n//d)
            break
    else:
        print (n, "是質數")


# Exercise ==> 改善上面的程式，使之可以印出質數的個數

#
# WHILE
#

count = 0
while count < 5:
    print('This will print 5 times')
    count += 1    # equivalent to 'count = count + 1'

