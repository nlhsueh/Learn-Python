#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# Set
# 用 {} 來放資料
# 沒有重複的資料, 資料沒有順序
# 用 Set() 來建立物件
# operatior: |, -, &, ^ 
# function: add(), remove(), intersection()...
# 

basketball_player = {"nick", "nick", "Nick", "albert"}
print (basketball_player)

baseball_player = {"nick", "john"}

basketball_palyer | baseball_player # 聯集
basketball_player.intersection(baseball_player)
basketball_palyer & baseball_player # 交集
basketball_palyer - baseball_player # 差集

basketball_player.add("jonathan")
print (basketball_player)

letter = set('hello')
letter.append('d')
print (letter)