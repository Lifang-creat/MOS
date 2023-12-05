#!/usr/bin/env python3
DEV=0
from flask import Flask, render_template, request,json
import sys
from datetime import datetime
import random
#sys.path.append('Service/')
import warnings
import os



warnings.filterwarnings("ignore")
# app = Flask(__name__, static_url_path='/static')
app = Flask(__name__, static_url_path='/')

@app.route("/", methods=['GET', 'POST'])
def main():
    with open("static/FastSpeech2/sample.txt", "r" ,encoding="utf-8") as f:
        lines = f.readlines()
    ranlist=[]
    for f in range(len(lines)):#len(lines) = 10 sample.txt中句子的个数
        ranlist.append(random.randint(3, 90)%2)#生成长度为1的[0,1,1,1,0,0...1,1]
    print(ranlist)

    #xz
    with open("static/FastSpeech2/sample.txt", "r" ,encoding="utf-8") as f:
        style_lines = f.readlines()
    stylelist=[]
    for f in range(len(style_lines)):#len(lines) = 10 sample.txt中句子的个数
        stylelist.append(random.randint(3, 90)%2)#生成长度为1的[0,1,1,1,0,0...1,1]
    print(stylelist)

    return render_template('index.html',lines=lines,ranlist=ranlist,style_lines=style_lines, stylelist=stylelist)
    # return render_template('index.html')




if __name__ == "__main__":
    app.run()


'''
IPv4 Address. . . . . . . . . . . : 192.168.100.8
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.100.1
   '''