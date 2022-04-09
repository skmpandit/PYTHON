# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:17:01 2022

@author: Sonu Kumar Mahto
"""

def amstrong(n):
    temp=n
    s=0
    c=0
    while n!=0:
        c=c+1
        n=n//10
    n=temp
    while n!=0:
        r=n%10
        n=n//10
        s=s+r**c
    if s==temp:
        print(temp," is Amstong number ")
####################################
for i in range(10,100000):
    amstrong(i)