# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:44:40 2022

@author: Sonu Kumar Mahto
"""

import pickle as pk
with open(r"E:\newfile\studentifo.txt", "rb") as put:
    rd=pk.load(put)
    print(rd)
    