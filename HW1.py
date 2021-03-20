# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:02:43 2021

@author: arthu
"""

print("第一題")
for i in range(5,0,-1):
    
    for a in range(0,i): 
        print("*",end="")
    print()
for i in range(2,6):
    
    for a in range(0,i): 
        print("*",end="")
    print()
print("程式執行完畢")

print("-"*30)

print("第二題")
print("第一小題:4的倍數")
A = int(input("請輸入1~100之間整數:"))
for i in range(1,100):  
    if i == A+1:
        break 
    if i%4 == 0:           
        print(i)
        print(i,"是4的倍數")
print()

print("第二小題:求質數")
A = int(input("請輸入整數:"))
if A > 1:
    for B in range(2,A):  
        if (A % B) == 0:
            print(A,"不是質數")
            break 
    else:                 
        print(A,"是質數")

else:
    print(A,"不是質數")
    
print("-"*30)

print("第三題")
import random

ans = random.randint(1,100)
guess = 0
chance = 0

while chance < 5:
    guess = int(input("輸入1-100之間整數:"))
    if guess > ans:
        print("介於",1,"~",guess,"之間")
        chance += 1
    elif guess < ans:
        print("介於",guess,"~",ans+1,"之間")
        chance += 1
    else:    
        print("猜對了")
        break
else:
    print("次數已用完")








