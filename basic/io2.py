# print to a file

f = open('output/io2.txt', 'w+')
print ('Hello world!', file=f)

f.close()