#
# IMPORTS 
#

# 'generic import' of math module
import math
math.sqrt(25)

# import a function
from math import sqrt
sqrt(25)    # no longer have to reference the module

# import multiple functions at once
from math import cos, floor

# import all functions in a module (generally discouraged)
from csv import *

# define an alias
import datetime as dt

# show all functions in math module
dir(math)

math.ceil(10.1) 	# 11