# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:36:00 2022

@author: Sonu Kumar Mahto
"""
import pickle as pk
with open(r"E:\newfile\studentifo.txt", "ab") as put:
    stu=[]
    ch='y'
    while ch=='y':
        n=input("Enter the student name: ")
        p=int(input("Enter the percentage: "))
        st=[n,p]
        stu.append(st)
        ch=input("do you want to contenue y/n ")
    pk.dump(stu,put)
put.close()
