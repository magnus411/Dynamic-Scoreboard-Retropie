# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:44:42 2022

@author: support
"""


#r"C:\Users\support\Documents\Mameflask\test.hi
import csv
import time
import os
import binascii
import shutil

lis =  []
#fresh = []
base = ["303132303030", "303039303030", "303038303030", "303035343030", "303033323030"]



def time_check():
    print("startet")
    tid = []
    
    tid.append(os.stat(r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi").st_mtime)

    while True:
        if os.stat(r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi").st_mtime == tid[0]:
            time.sleep(3)
            print("sleeping")
        else:
            print("den er endret!!!")
            read_score()
            break

    


def read_score():
    with open(r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi", 'rb') as f:
        
        
        fresh = []
        
        hexdata = binascii.hexlify(f.read())
        hexa_string = hexdata.decode('ascii')
        
        fresh.append(hexa_string[14:26])
        fresh.append(hexa_string[82:94])
        fresh.append(hexa_string[150:162])
        fresh.append(hexa_string[218:230])
        fresh.append(hexa_string[286:298])
        
        
        new = []
        
        for i in fresh:
            exist_count = base.count(i)

            if exist_count == 0:
                new.append(i)
                
        
        
        
        #fresh = hexa_string[14:26]
        f.close()

        #fresh = (hexa_string[14:26], hexa_string[82:94], hexa_string[150:162], hexa_string[218:230], hexa_string[286:298])
        
        
        #check(fresh)
        if len(new) == 0:
            print("ingen endring i score")
            time_check()

        else:
            add_score(new[-1])

    
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
    with open(r'/home/pi/RetroPie/web/leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([h2a])
    
    
    src = r"/home/pi/RetroPie/web/dkong3.hi"
    dst = r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi"
    #os.unlink(r"\\retropie\roms\arcade\mame2003\hi\dkong3.hi")
    os.remove(r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi")
    shutil.copy(src, dst)
    
    file.close()
    #time_check()


def check(fresh):
    #player_name = input("Skriv inn navnet ditt her: ")

    for i in range(5):
        print(i)
        
        if str(fresh) == str(base[i]):
           print("lik")
           print(fresh)
           
           print(base[i][1])
           
        else:
            
            print("ulik")
            print(fresh)
            
            break
              
                    
            #print("ulik")
            #print(base[i][1])
            #print(fresh[i])
            #add_score(fresh[i])
        
            
#add_score("313232333130")
time_check()
#if __name__ == "__main__":


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

