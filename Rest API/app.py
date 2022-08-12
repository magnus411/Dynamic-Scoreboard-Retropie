from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS,cross_origin
import threading



import csv
import time
import os
import binascii
import shutil

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


####################

base = ["303132303030", "303039303030", "303038303030", "303035343030", "303033323030"]
lis =  []

data = "tall"

def time_check():
    print("startet")
    tid = []
    


     ############################
            #DKONG3.hi Ligger et annet sted!!!!!
            #
            #r"/home/pi/RetroPie/roms/arcade/mame2003/hi/dkong3.hi"
    ############################




    tid.append(os.stat("dkong3.hi").st_mtime)

    while True:
        if os.stat("dkong3.hi").st_mtime == tid[0]:
            time.sleep(3)
            print("sleeping")
        else:
            print("den er endret!!!")
            read_score()
            break

    


def read_score():
    with open("dkong3.hi", 'rb') as f:
        
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
                
        f.close()

        if len(new) == 0:
            print("ingen endring i score")
            time_check()

        else:
            add_score(new[-1])


def add_score(n):
    
    h2a = bytes.fromhex(n).decode('utf-8')

    global data
    data = h2a
    time_check()
    return data
    
#####################
####################



class Data(Resource):





    def get(self):

        #data = pd.read_json('data.json')  # read CSV
        #data = data.to_dict()  # convert dataframe to dictionary

        return {'data': data}, 200  # return data and 200 OK code

api.add_resource(Data, '/Data')  # '/users' is our entry point for Users




t=threading.Thread(target=time_check)
t.start()
app.run()
#if __name__ == '__main__':
    #a = Thread(target = time_check)
    #b = Thread(target = app.run)

    #time_check()

    #app.run()  # run our Flask app 
