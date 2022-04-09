# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:39:18 2022

@author: Sonu Kumar Mahto
"""
with open(r"E:\newfile\story.txt","r") as fp:
    #fp=open(r"E:\newfile\story.txt","r")
    fp2=open(r"E:\newfile\Banana.txt","w")
    for i in fp:
        print(type(i))
'''n=fp.read()
wd=n.split()
for i in wd:
    if i[0] not in ['a','A']:
        fp2.write(i+" ")
print("File Copyed ---\n")
fp.close()
fp2.close()
'''
