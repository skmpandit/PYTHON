# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 01:04:40 2022

@author: Sonu Kumar Mahto
"""

n = int(input("Enter the number: "))

flag = False

if n > 1:
    for i in range(2,n):
        if (n%i)==0:
            flag=True
            break
if flag:
    print(n," is not a prime number")
else:
    print(n," is prime number")