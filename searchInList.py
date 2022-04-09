# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:55:44 2022

@author: Sonu Kumar Mahto
"""

LT=eval(input("Enter the List value"))

val=input("Enter the search value")

for i in LT:
    if val==str(i):
        print(val," Found in the List")
        break
else:
    print(val," Not found")