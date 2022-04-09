# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:49:49 2022

@author: Sonu Kumar Mahto
"""

term = int(input("Enter the your last term : "))
n1=0
n2=1
n3=3
count=0
if term <= 0 or term == 0 or term == 1 or term == 2:
    print("Opps! Please enter the number greater than 3",)
else:
    print(n1)
    while count < term:
        print(n2)
        nth=n1+n2+n3
        n1=n2
        n2=n3
        n3=nth
        count+=1
    