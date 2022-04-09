# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:53:27 2022

@author: Sonu Kumar Mahto
"""

def add(stu):
    r=int(input("Enter the Roll Number: "))
    n=input("Enter the student name: ")
    d=input("Enter the department: ")
    s=int(input("Enter the subject: "))
    p=int(input("Enter the percentage: "))
    st=[r,n,d,s,p]
    stu.append(st)
    display(stu)    
def display(stu):
    print("\n\nYour listed data: ",stu)
    
def delete(stu):
    x = int(input("Enter the roll number for delete: "))
    k=0
    for i in stu:
        if i[0]==x:
            stu.pop(k)
        else:
            k=k+1      
    
stu=[]
n='y'
while n=='y':
    x=int(input("\n 1 to insert \n 2 diplay\n 3 delete \n Enter what you want:- "))
    if x==1:
        add(stu)
    elif x==2:
        display(stu)
    elif x==3:
        delete(stu)
    n=input("Do you Want to Contenue  y/n ")
    