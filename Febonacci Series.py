# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:37:06 2022

@author: Sonu Kumar Mahto
"""
term = int(input("How many time you want to print Febonacci Series: "))
n1=0
n2=1
count=0

if term <= 0:
    print("Opps! Please enter the number greater than 0")
elif term == 1:
    print("Fibonacci series up to ",term," :")
else:
    print("Fibonacci Series:")
    while count < term:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1