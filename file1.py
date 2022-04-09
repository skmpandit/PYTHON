# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:14:32 2022

@author: Sonu Kumar Mahto
"""

fp=open(r"E:\newfile\story.txt","a")
n=' '
print("Enter in File---\n")
while n!='#':
    n=input()
    fp.write(n)
    fp.write("\n")
fp.close()
