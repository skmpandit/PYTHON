# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:54:59 2022

@author: Sonu Kumar Mahto
"""

num = int(input("Enter a number: "))

 
if num > 1:
    
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
 
else:
   print(num,"is not a prime number")
    