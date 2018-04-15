#
# SETS 
# properties: unordered, iterable, mutable, can contain multiple data types
# made of unique elements (strings, numbers, or tuples)
# like dictionaries, but with keys only (no values)
#

# Create a set
basketball = set() # an empty set
basketball = {"nick", "nick", "Nick", "albert"} # nick, Nick, Albert
baseball = set(["nick", "john"]) # create from a list

# Examine a set
len(basketball)					# returns 3
'nick' in languages			# returns True
for player in basketball:
	print (player)

# Set operations
basketball | baseball 	# 聯集
basketball.intersection(baseball) # 交集
basketball & baseball 	# 交集
basketball - baseball 	# 差集

# Modify a set (does not return the set)
basketball.add('alex')	# add a new element
basketball.add('alex')	# add an existing element (ignored, no error)
basketball.remove('nick')	# remove an element
basketball.remove('jonathan')	# remove a non-existing element (throws an error)
basketball.discard('jonathan')	# remove an element if present, but ignored otherwise
basketball.pop()	# remove and return an element
basketball.clear()	# remove all elements

# Get a sorted list of unique elements from a list
s2 = sorted(set([9, 0, 2, 1, 0]))	# returns [0, 1, 2, 9]