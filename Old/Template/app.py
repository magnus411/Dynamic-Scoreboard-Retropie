# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:42:40 2022

@author: support
"""
import csv
import numpy as np

from flask import Flask, render_template, request, jsonify, redirect
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit, send
import sys
import os
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret!"
socketio = SocketIO(app)



    #print(score_list)
    
    
    
headings = ("Score", "Name")
# = (("magnus", 2000), ("david", 1000), ("Jonas", 40000))











@socketio.on("reload")
def reload():
    sa = "asdsd"
    socketio.emit("reload", sa, broadcast=True)

    
@socketio.on("connect")
def ws_connect():
    tem = "HEIIII"
    socketio.emit("user", tem, broadcast=True)
        
        



    
@app.route('/Name', methods=["POST", "GET"])
def getName(): 
    with open(r'/home/pi/RetroPie/web/leaderboard.csv', 'r', newline='') as file:
        data2 = list(csv.reader(file))
        last = data2[-1]
        print(data2)
        

    name = request.form.get("name")
    if request.method == "POST":
        data2.append((int(last[0]), str(name)))
        print(name + "ADDED IN THE LIST")
        print(data2)
        #data2.sort(reverse=True)
        reload()
        with open(r'/home/pi/RetroPie/web/leaderboard2.csv', 'a', newline='') as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow((int(last[0]), str(name)))
        #name = None

        return redirect("/")

        
        
    return render_template("form.html", name=name, last=last)    
        
    

@app.route('/GetData', methods=["POST"])
def GetData():
    
    #name = request.form.get("name")
    #print(name)
    return jsonify({"name": "newName"})    
    
    

@app.route("/")
def home():
    with open(r'/home/pi/RetroPie/web/leaderboard2.csv', 'r', newline='') as file:
        data2 = list(csv.reader(file))

    
    c = []
    for i in range(len(data2)):
        b = int(data2[i][0])
        c.append([b, data2[i][1]])



    c.sort(reverse=True)


    #data4 = sorted(data2, reverse=True)
    #data2.sort(reverse=True)
    #print(data2)
  
    return render_template("scoreboard.html", headings=headings, data=c)


if __name__ == "__main__":
    socketio.run(app)
