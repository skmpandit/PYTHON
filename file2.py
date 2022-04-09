# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:54:01 2022

@author: Sonu Kumar Mahto
"""

with open(r"E:\newfile\copycontent1.txt", "r") as input1:
    with open(r"E:\newFile\copycontent2.txt", "w") as output:
        for line in input1:
            output.write(line)