# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:19:10 2022

@author: Sonu Kumar Mahto
"""

LT=eval(input("Enter the List value"))

x=len(LT)

LT=LT[x-3:]+LT[:x-3]

print(LT)