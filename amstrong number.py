# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:47:58 2022

@author: Sonu Kumar Mahto
"""

n = int(input("Enter amstrong number: "))
temp=n
s=0

while n!=0:
    r=n%10
    n=n//10
    s=s+r**3
if s==temp:
    print(s," is amstrong number")
else:
    print(s," is not a prime number")