# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:35:00 2022

@author: Sonu Kumar Mahto
"""

def add(stu):
    r=int(input("Enter the Roll number :- "))
    nm=input("Enter the name ")
    per=int(input("Enter the Percentage  :- "))
    st=[r,nm,per]
    stu.append(st)
    
def diplay(stu):
    print(" Student infromation \n ",stu)

#####################################
stu=[]
n='y'
while n=='y':
    x=int(input("\n 1 to insert \n 2 diplay "))
    if x==1:
        add(stu)
    elif x==2:
        display(stu)
    n=input("Do you Want to Contenue  y/n ")
    