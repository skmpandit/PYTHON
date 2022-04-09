# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:13:22 2022

@author: Sonu Kumar Mahto
"""

n = int(input('Enter a Number : '))
temp=n
s=0
while n!=0:
    r=n%10
    n=n//10
    s=s*10+r
print(s)