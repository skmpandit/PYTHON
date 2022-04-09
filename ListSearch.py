# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:59:52 2022

@author: Sonu Kumar Mahto
"""

List = eval(input("Enter the list : "))

x = int(input("Enter the search value: "))

for i in List:
    if(i==x):
        print(x, "value is found")
        break
else:
    print(x,"value is not found")
    