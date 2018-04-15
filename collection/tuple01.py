# Create a tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = tuple([1, 2, 3, 4, 5]) 	#create from list
tup2[0] = 100			# ERROR

# Get the elements
print (tup1[0])
print (tup2[1:4])		# 2, 3, 4 

# Function and method
len (tup2) 		# 5
tup2.count(1)	# 1
tup2.index(1)	# 0
tup2 = tup2 + tuple([6])	# ok(1,2,3,4,5,6)
tup2 = tup2 + (6)	# error

(3, 4) * 2  		   # returns (3, 4, 3, 4)

# Sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
s2 = sorted(tens)	# sorts by first element in tuple, then second

# Tuple unpacking
bart = ('male', 10, 'simpson')  # create a tuple
(sex, age, surname) = bart      # assign three values at once
sex, age, surname = bart        # assign three values at once
t1