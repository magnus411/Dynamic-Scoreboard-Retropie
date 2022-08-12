# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:44:42 2022

@author: support
"""


#r"C:\Users\support\Documents\Mameflask\test.hi
import csv
import pandas as pd
import time
import os
import binascii

lis =  []
#fresh = []
base = ([14, "303132303030"],[82, "303039303030"],[150, "303038303030"],[218, "303035343030"],[286, "303033323030"])




def time_check():
    tid = []
    
    tid.append(os.stat(r"\\retropie\roms\arcade\mame2003\hi\dkong3.hi").st_mtime)

    while True:
        if os.stat(r"\\retropie\roms\arcade\mame2003\hi\dkong3.hi").st_mtime == tid[0]:
            time.sleep(3)
            print("sleeping")
        else:
            print("den er endret!!!")
            read_score()
            break

    


def read_score():
    with open(r"\\retropie\roms\arcade\mame2003\hi\dkong3.hi", 'rb') as f:
        
        
        
        hexdata = binascii.hexlify(f.read())
        hexa_string = hexdata.decode('ascii')
        
        #fresh.append(hexa_string[14:26])
       # fresh.append(hexa_string[82:94])
        #fresh.append(hexa_string[150:162])
       # fresh.append(hexa_string[218:230])
        #fresh.append(hexa_string[286:298])
        
        
        fresh = (hexa_string[14:26], hexa_string[82:94], hexa_string[150:162], hexa_string[218:230], hexa_string[286:298])
        check(fresh)
    
    
        #print(score1)
        #print(score2)
        #print(score3)
        #print(score4)
        #print(score5)
    
        #print(hexdata)
        #print(h2a)


def add_score(n):
    
    h2a = bytes.fromhex(n).decode('utf-8')

    
    
    #Append to the csv.
    with open(r'C:\Users\support\Documents\Mameflask\leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((h2a, "hey"))
    
    os.remove(r"\\retropie\roms\arcade\mame2003\hi\dkong3.hi")

    

def check(fresh):
    #player_name = input("Skriv inn navnet ditt her: ")

    for i in range(5):
        print(i)
        if str(base[i][1]) == str(fresh[i]):
            
            print("lik")
        else:
            print("ulik")
            #print(base[i][1])
            #print(fresh[i])
            add_score(fresh[i])
        
            

time_check()
#read_score()




## DELETE FILE AFTER
# CHECK LEADERBOARD FOR DUPLICATES AND UPDATE





# Append to the csv.
#with open(r'C:\Users\support\Documents\Mameflask\leaderboard.csv', 'a', newline='') as file:
    #writer = csv.writer(file)
    #writer.writerow((h2a, player_name))

# Read the csv.
#with open(r'C:\Users\support\Documents\Mameflask\leaderboard.csv', 'r', newline='') as file:
    #score_list = list(csv.reader(file))
    #for row in score_list:
        #print(row)

