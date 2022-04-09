# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:14:08 2022

@author: Sonu Kumar Mahto
"""

fp=open(r"E:\newfile\copycontent1.txt","r")
s=0
n=fp.read()
wd=n.split()
for i in wd:
    if i[0].isdigit():#ord(i[0])>=48 and ord(i[0])<58:
        print(i," + ",end="")
        s=s+int(i)
print(" = ",s)