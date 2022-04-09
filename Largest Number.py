# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:36:58 2022

@author: Sonu Kumar Mahto
"""

n1 = int(input("Enter your fist number: "))
n2 = int(input("Enter your second nubmer: "))
n3 = int(input("Enter your third number: "))

largest=0

if n1 >= n2 and n1 >= n3:
    largest=n1
elif n2 >= n1 and n2 >= n3:
    largest=n2
else:
    largest=n3
print(largest," is the largest number")