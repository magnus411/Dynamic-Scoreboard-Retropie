# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:44:42 2022

@author: support
"""


#r"C:\Users\support\Documents\Mameflask\dkong3.hi

import csv

with open(r'C:\Users\support\Documents\Mameflask\leaderboard.csv', 'r', newline='') as file:
    score_list = list(csv.reader(file))
    print(score_list)
