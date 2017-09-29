#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nlhsueh
"""




# i=0
# a="abcdefghijklmnopqrstuvwxyz"
# for x in a:
# 	# print (x)
# 	i = i+1
# 	if i%10==0:
# 		print (x)
# print (i)




# exception handle

try:
	age = int(input("your age: "))
	gradeBook = open('utility1.py');
	print (gradeBook);
except ValueError:
	print ("Error, please input another one")
	age = int(input("your age: "))
except IOError:
	print ("IO error, please check the file")

print (age)



# == modules
# from utility import multiply
# import utility

# print str(utility.multiply(2,2))

# p1 = utility.Person("Nick",12)
# print p1


# == inheritance
# class Person:
	# def __init__(self, name, age):
# 		self.name = name;
# 		self.age = age;

# 	def __str__ (self):
# 		return self.name + ' ' + str(self.age)

# 	def show(self):
# 	 	print self;

# 	def changeAge(self, a):
# 	 	self.age = a

# 	def sayhi(self):
# 		print "hi"

# class Engineer(Person):
# 	def __init__(self,name,age,pg):
# 		Person.__init__(self,name,age)
# 		self.pg = pg

# 	def __str__(self):
# 		s = Person.__str__(self)
# 		return  s+", " + self.pg

# 	def getPG(self):
# 		return self.pg;    

# p = Person('Nick',20)
# p.changeAge(100)
# p.show();
# p.sayhi()

# eng = Engineer('Nick', 12, 'Java')
# print eng
# print eng.getPG()
