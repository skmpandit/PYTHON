# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:29:37 2022

@author: Sonu Kumar Mahto
"""

term = int(input("How many time you want to print this sereis: "))
n1=0
n2=2
count=0

if term<=0 or term==1 or term==2:
    print("Opps! Please enter the number greater than ",n2)
else:
    print("Your Series: ")
    while count < term :
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        