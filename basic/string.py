# STRINGS 
# properties: iterable, immutable

# create a string
s = str(42)         # convert another data type into a string
s = 'I like python'
s = "I like python"	# ' and " are both ok

# examine a string
s[0]                # returns 'I'
len(s)              # returns 10

# string slicing is like list slicing
s[:6]               # returns 'I like'
s[7:]               # returns 'python'
s[-1]               # returns 'n'

# basic string methods (does not modify the original string)
s.lower()           # returns 'i like python'
s.upper()           # returns 'I LIKE PYTHON'
s.startswith('I')   # returns True
s.endswith('python')# returns True
s.isdigit()         # returns False (returns True if every character in the string is a digit)
s.find('like')      # returns index of first occurrence (2)
s.find('hate')      # returns -1 since not found
s.replace('like', 'love')    # replaces all instances of 'like' with 'love'

# split a string into a list of substrings separated by a delimiter
s.split(' ')        # returns ['I', 'like', 'python']
s.split()           # equivalent (since is the default delimiter)
s2 = 'a, an, the'
s2.split(',')       # returns ['a', ' an', ' the']

# join a list of strings into one string using a delimiter
stooges = ['larry', 'curly', 'moe']
' '.join(stooges)   # returns 'larry curly moe'
':'.join(stooges)   # returns 'larry:curly:moe'

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'

# remove whitespace from start and end of a string
s5 = '  ham and cheese  '
s5.strip()          # returns 'ham and cheese'

# string substitutions/formating
'raining %s and %s' % ('cats', 'dogs')
'raining {} and {}'.format('cats', 'dogs')
'raining {1} and {0}'.format('dogs', 'cats') # using index
'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs') # named arguments

# string formatting
'pi is {:.2f}'.format(3.14159)      # returns 'pi is 3.14'

# escape code
s= "he doesn't like apple"
s = 'he doesn\'t like apple'

# use () to connect two line string
text = ('Today I will talk a long story. '
        'Long time ago, there is a king called Tom, he...')

text = 'Today I will talk a long story. ' + \
       'Long time ago, there is a king called Tom, he...'

# normal strings versus raw strings
print('first line\nsecond line')    
print(r'first line\nfirst line') # raw string

# no new line
print ('I like apple', end='')
print (' and banana')