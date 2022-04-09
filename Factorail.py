# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:44:10 2022

@author: Sonu Kumar Mahto
"""

n = int(input("Enter your number: "))

factorial=1

if n < 0:
    print("Factorial is not posible from negative number: ")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial= factorial*i
    print("The factorial of ",n," is ",factorial)