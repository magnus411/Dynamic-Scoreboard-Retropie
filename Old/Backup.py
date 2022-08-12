# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:58:47 2022

@author: support
"""


@app.route('/form', methods=["POST", "GET"])
def form():
    data.append([request.form.get("n1"), "asd"])
    
    with open(r'C:\Users\support\Documents\Mameflask\leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("n1")))
    
    