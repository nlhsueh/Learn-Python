# lamda

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
print (pairs)
pairs.sort()
print (pairs)

pairs = [(4, 'four'), (1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key = lamda pair: pair[1])
print (pairs)