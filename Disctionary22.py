# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:11:11 2022

@author: Sonu Kumar Mahto
"""

stu=[]
n='y'
while n=='y':
    r=int(input("Enter the Roll number :- "))
    nm=input("Enter the name ")
    per=int(input("Enter the Percentage  :- "))
    st=[r,nm,per]
    stu.append(st)
    n=input("Do you Want to Contenue  y/n ")
print(" Student infromation \n ",stu)
    