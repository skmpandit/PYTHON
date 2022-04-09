# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:15:43 2022

@author: Sonu Kumar Mahto
"""

term = int(input("How many time you want to print series: "))
n1=0
n2=1
n3=2

count=0

if term <=0 and term==1 and term==2:
    print("Opps! Please enter term greater than ",n2)
else:
    print("Your series: ")
    print(n1)
    while count <= term:
        print(n2)
        nth=n1+n2+n3
        n1=n2
        n2=n3
        n3=nth
        count+=1