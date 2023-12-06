#!/usr/bin/env python3
DEV=0
from flask import Flask, render_template, request,json
import sys
from datetime import datetime
import random
#sys.path.append('Service/')
import warnings




warnings.filterwarnings("ignore")
app = Flask(__name__, static_url_path='/static')



@app.route("/", methods=['GET', 'POST'])
def main():
    with open("static/sample.txt", "r" ,encoding="utf-8") as f:
        lines = f.readlines()
    ranlist=[]
    for f in range(len(lines)):
        ranlist.append(random.randint(3, 90)%2)
    print(ranlist)

    with open("static/FastSpeech2/sample.txt", "r" ,encoding="utf-8") as f:
        style_lines = f.readlines()
    stylelist=[]
    for f in range(len(style_lines)):#len(lines) = 10 sample.txt中句子的个数
        stylelist.append(random.randint(3, 90)%2)#生成长度为1的[0,1,1,1,0,0...1,1]
    print(stylelist)

    # return render_template('index.html',lines=lines,ranlist=ranlist,style_lines=style_lines, stylelist=stylelist )


@app.route("/thank", methods=['GET', 'POST'])
def thank():
    if request.method == 'GET':
        res=dict(request.args)
        #print(res)

        name = res['lname']#wlf

        MOS_TRUTH_N=0
        MOS_VOCODER_N=0
        MOS_BASE_N=0
        MOS_T_STYLER_N=0

        MOS_TRUTH_E=0
        MOS_VOCODER_E=0
        MOS_BASE_E=0
        MOS_T_STYLER_E=0
        MOS_Style_Similarity = ''
        MOS_Speaker_Similarity = ''

        for i in range(5):
            geta='Truth-Naturalness-'+str(i)
            MOS_TRUTH_N=MOS_TRUTH_N+int(res[geta])
            getb='Vocoder-Naturalness-'+str(i)
            MOS_VOCODER_N=MOS_VOCODER_N+int(res[getb])
            getc='T_STYLER-Naturalness-'+str(i)
            MOS_T_STYLER_N=MOS_T_STYLER_N+int(res[getc])
            getd='FastSpeech2-Naturalness-'+str(i)
            MOS_BASE_N=MOS_BASE_N+int(res[getd])
            gete='Truth-Expressiveness-'+str(i)
            MOS_TRUTH_E=MOS_TRUTH_E+int(res[gete])
            getf='Vocoder-Expressiveness-'+str(i)
            MOS_VOCODER_E=MOS_VOCODER_E+int(res[getf])
            getg='T_STYLER-Expressiveness-'+str(i)
            MOS_T_STYLER_E=MOS_T_STYLER_E+int(res[getg])
            geth='FastSpeech2-Expressiveness-'+str(i)
            MOS_BASE_E=MOS_BASE_E+int(res[geth])
            geti='Style_Similarity-'+str(i)
            MOS_Style_Similarity=MOS_Style_Similarity+str(res[geti])
            getj='Speaker_Similarity-'+str(i)
            MOS_Speaker_Similarity=MOS_Speaker_Similarity+str(res[getj])



        MOS_TRUTH_N=MOS_TRUTH_N/float(5)
        MOS_VOCODER_N=MOS_VOCODER_N/float(5)
        MOS_T_STYLER_N=MOS_T_STYLER_N/float(5)
        MOS_BASE_N=MOS_BASE_N/float(5)
        MOS_TRUTH_E=MOS_TRUTH_E/float(5)
        MOS_VOCODER_E=MOS_VOCODER_E/float(5)
        MOS_T_STYLER_E=MOS_T_STYLER_E/float(5)
        MOS_BASE_E=MOS_BASE_E/float(5)

        now = str(datetime.now())

        # print(now)
        # print(MOS_TACO) 
        # print(MOS_TRUTH)

        MOS_TRUTH_N=float("{:.2f}".format(MOS_TRUTH_N))
        MOS_VOCODER_N=float("{:.2f}".format(MOS_VOCODER_N))
        MOS_T_STYLER_N=float("{:.2f}".format(MOS_T_STYLER_N))
        MOS_BASE_N=float("{:.2f}".format(MOS_BASE_N))
        MOS_TRUTH_E=float("{:.2f}".format(MOS_TRUTH_E))
        MOS_VOCODER_E=float("{:.2f}".format(MOS_VOCODER_E))
        MOS_T_STYLER_E=float("{:.2f}".format(MOS_T_STYLER_E))
        MOS_BASE_E=float("{:.2f}".format(MOS_BASE_E))

        with open("static/result/"+name,'w+',encoding="utf-8") as fw:
            fw.write(now+"\n")
            fw.write(str(name)+"\n")
            fw.write("Truth-Naturalness : "+str(MOS_TRUTH_N)+"\n")
            fw.write("Vocoder-Naturalness: "+str(MOS_VOCODER_N)+"\n")
            fw.write("T_STYLER-Naturalness: "+str(MOS_T_STYLER_N)+"\n")
            fw.write("FastSpeech2-Naturalness: "+str(MOS_BASE_N)+"\n")
            fw.write("Truth-Expressiveness: "+str(MOS_TRUTH_E)+"\n")
            fw.write("Vocoder-Expressiveness: "+str(MOS_VOCODER_E)+"\n")
            fw.write("T_STYLER-Expressiveness: "+str(MOS_T_STYLER_E)+"\n")
            fw.write("FastSpeech2-Expressiveness: "+str(MOS_BASE_E)+"\n")
            fw.write("Style Similarity: "+str(MOS_Style_Similarity)+"\n")
            fw.write("Speaker Similarity: "+str(MOS_Speaker_Similarity)+"\n")

        with open("static/result/user",'a+',encoding="utf-8") as fw:
            fw.write(name+"\n")
        res="Truth-Naturalness : "+str(MOS_TRUTH_N)+"  "+"Vocoder-Naturalness: "+str(MOS_VOCODER_N)+"  "+"T_STYLER-Naturalness: "+str(MOS_T_STYLER_N)+"  "+"FastSpeech2-Naturalness: "+str(MOS_BASE_N)+"  "+"Truth-Expressiveness: "+str(MOS_TRUTH_E)+"  "+"Vocoder-Expressiveness: "+str(MOS_VOCODER_E)+"  "+"T_STYLER-Expressiveness: "+str(MOS_T_STYLER_E)+"  "+"FastSpeech2-Expressiveness: "+str(MOS_BASE_E)+"  "+"MOS_Style_Similarity: "+str(MOS_Style_Similarity)+"  "+"MOS_Speaker_Similarity: "+str(MOS_Speaker_Similarity)
    return render_template('thank.html', res=res)


@app.route("/results", methods=['GET', 'POST'])
def results():
    user=[]
    with open("static/result/user","r",encoding="utf-8") as f:
        user=f.read().splitlines()
    JS=[]
    for i in list(set(user)):
        with open("static/result/"+str(i), "r" ,encoding="utf-8") as f:
            lines = f.read()
            JS.append(lines.replace("\n","\t"))
    return render_template('results.html',JS=JS)

@app.route("/mos", methods=['GET', 'POST'])
def mos():
    user=[]
    with open("static/result/user","r",encoding="utf-8") as f:
        user=f.read().splitlines()
    JS=""
    MOS_TRUTH_N=0
    MOS_VOCODER_N=0
    MOS_BASE_N=0
    MOS_T_STYLER_N=0

    MOS_TRUTH_E=0
    MOS_VOCODER_E=0
    MOS_BASE_E=0
    MOS_T_STYLER_E=0
    MOS_Style_Similarity=''
    MOS_Speaker_Similarity=''

    user_ =0
    if len(user) ==0:
        return render_template('mos.html',JS="No valid user now")
    for i in list(set(user)):
        
        if i[0]=="_":
            continue
        user_+=1    
        with open("static/result/"+str(i), "r" ,encoding="utf-8") as ff:
            lines = ff.read().splitlines()
            #print(float(lines[2]))
            # MOS_TACO=MOS_TACO+float(lines[2])
            # MOS_TRUTH=MOS_TRUTH+float(lines[3])

            MOS_TRUTH_N=MOS_TRUTH_N+float(lines[2])
            MOS_VOCODER_N=MOS_VOCODER_N+float(lines[3])
            MOS_T_STYLER_N=MOS_T_STYLER_N+float(lines[4])
            MOS_BASE_N=MOS_BASE_N+float(lines[5])
            MOS_TRUTH_E=MOS_TRUTH_E+float(lines[6])
            MOS_VOCODER_E=MOS_VOCODER_E+float(lines[7])
            MOS_T_STYLER_E=MOS_T_STYLER_E+float(lines[8])
            MOS_BASE_E=MOS_BASE_E+float(lines[9])
            MOS_Style_Similarity=str(lines[10])
            MOS_Speaker_Similarity=str(lines[11])

    if len(list(set(user))) > 0 :
        JS = "MOS of Truth-Naturalness is: " + str(float("{:.2f}".format(MOS_TRUTH_N/float(user_)))) + "\n"
        JS +="MOS of Vocoder-Naturalness is: " + str(float("{:.2f}".format(MOS_VOCODER_N/float(user_)))) + "\n"
        JS +="MOS of T_STYLER-Naturalness is: " + str(float("{:.2f}".format(MOS_T_STYLER_N/float(user_)))) + "\n"
        JS +="MOS of FastSpeech2-Naturalness is: " + str(float("{:.2f}".format(MOS_BASE_N/float(user_)))) + "\n"
        JS +="MOS of Truth-Expressiveness is: " + str(float("{:.2f}".format(MOS_TRUTH_E/float(user_)))) + "\n"
        JS +="MOS of Vocoder-Expressiveness is: " + str(float("{:.2f}".format(MOS_VOCODER_E/float(user_)))) + "\n"
        JS +="MOS of T_STYLER-Expressiveness is: " + str(float("{:.2f}".format(MOS_T_STYLER_E/float(user_)))) + "\n"
        JS +="MOS of FastSpeech2-Expressiveness is: " + str(float("{:.2f}".format(MOS_BASE_E/float(user_)))) + "\n"
        JS +="MOS of Style Similarity is: " + str(MOS_Style_Similarity) + "\n"
        JS +="MOS of Speaker Similarity is: " + str(MOS_Speaker_Similarity) + "\n"

    return render_template('mos.html',JS=JS)

if __name__ == "__main__":
    app.run()


'''
IPv4 Address. . . . . . . . . . . : 192.168.100.8
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.100.1
   '''
