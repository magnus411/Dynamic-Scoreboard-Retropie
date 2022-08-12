# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:25:32 2022

@author: support
"""


new = []
import binascii
fresh = []
import csv


base = ["303132303030", "303039303030", "303038303030", "303035343030", "303033323030"]
#base = [303132303030, 303039303030, 303038303030, 303035343030, 303033323030]


for i in range(5):
   
    h2a = bytes.fromhex(base[i]).decode('utf-8')
    print(h2a)
     

    
