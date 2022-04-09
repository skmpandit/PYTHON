# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:34:52 2022

@author: Sonu Kumar Mahto
"""

n = int(input("Enter a number: "))
temp= n
s=0
while n!=0:
    r=n%10
    n=n//10
    s=s*10+r
    
if s==temp:
    print(s," is palidrom number")
else:
    print(s," is not palidrom numberw")