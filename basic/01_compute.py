#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# 基本運算
#

1+1

50-8*10

(90-30)/11

(90-30)//11 # floor division, 忽略小數

round ((90-30)/11) # 四捨五入

round(5.5)

round(5.49)

5**2  # 平方

import math

math.ceil(10.1) # 無條件進入

"""
Exercise
* 計算學生的成績平均成績：10, 30, 40, 90, 100, 60
* 四捨五入，無條件進入法、無條件捨去法
"""

#
# 變數
#

width = 100
height = 20
print (width * height)

area = width * height
print (area) # access to a undefined variable

"""
Exercise
* 計算學生的成績平均成績：10, 30, 40, 90, 100, 60
* 計算這些分數的標準差
"""

# 
# 跨行連接
# 

english=1
math=2
phy=4

total_grade = 	\
 english + \
math + \
   phy  						
