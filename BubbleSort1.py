# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:28:57 2022

@author: Sonu Kumar Mahto
"""

List = eval(input("Enter your list : "))

for i in range(len(List)):
    for j in range((len(List)-i-1)):
        if List[j] < List[j+1]:
            temp = List[j]
            List[j] = List[j+1]
            List[j+1] = temp
print(List)