# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:53:45 2021

@author: user
"""

'''
串列中有的元素才能使用index,不然會error

'''

fruits = ["apple","banana","orange","cherry"]

n = fruits.index("orange") #index索引值

print(n)


name = input("輸入水果名稱:")
if fruits.count(name) != 0:
    print("{}在索引值:{}".format(name,fruits.index(name)))
else:
    print("找不到")










