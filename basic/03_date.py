#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# time
# 

import time
time.time()
time.localtime()
time.asctime()
time.asctime(time.localtime())
time.sleep(3)

import calendar
cal = calendar.month(2018,1)
print (cal)

# 
# datetime
# 

from datetime import date
d = date.today()
t = d.timetuple()
t
for x in t:
    print (x)

d.isoformat()