# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input('Enter a year : '))
if n%4==0 and n%100!=0 or n%400==0:
    print (n, " is leapyear ")
else:
    print(n, " is not leapyear ")