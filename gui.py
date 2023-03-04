####Authors:
####Aloke Kumar Das, Chandiprasad Kar ############
####email "das21aloke@gmail.com"
# !/usr/bin/python3  


import io
import serial
import time
import sys
import csv
import numpy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

from optparse import OptionParser
import serial.tools.list_ports as port_list

import tkinter
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  


def runTest():
    print(en1.get())
    print(en2.get())
    print(en3.get())
    print("Start Volt,",en1.get())
    print("End Volt,",en2.get())
    print("Volt StepSize,",en3.get())
    V_b=int(en1.get())
    V_e=int(en2.get())
    V_step=int(en3.get())

    finaloutput=[]
       
    ports = list(port_list.comports())
    for p in ports:
        print (p)

    ser = serial.Serial()
    ser.port = "COM6"
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    ser.parity = serial.PARITY_NONE #set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    #ser.timeout = None          #block read
    ser.timeout = 1            #non-block read
    #ser.timeout = 2              #timeout block read
    ser.xonxoff = False    #disable software flow control
    ser.rtscts =  False  #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    #ser.writeTimeout = 2    #timeout for write


    try: 
        ser.open()
    except (Exception):
        print("error open serial port: " )
        exit()

    eol_char='\r\n'
    sio=io.TextIOWrapper(io.BufferedReader(ser),newline=eol_char)
    if ser.isOpen():
        print("opened successfully: " )
    else:
        print("cannot open serial port ")

    starting="D1=10"
    ser.write((starting+eol_char).encode('utf-8'))
    time.sleep(0.2)
    thresold_Curr='C1=0.5E-3'
    ser.write((thresold_Curr+eol_char).encode('utf-8'))
    time.sleep(0.2)
    starting_Kill='T1=1'
    ser.write((starting_Kill+eol_char).encode('utf-8'))
    time.sleep(0.2)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []


    for incre in range(V_b, V_e+V_step, V_step):
        mindata=[]    
        print("Voltage:"+str(incre)+"\n")    
        sending = "D1="+str(incre)
        ser.write((sending+eol_char).encode('utf-8'))
        time.sleep(0.2)
        ans=sio.read()
        sys.stdout.write('recieved:'+str(ans))
        ## Measure voltage after setting
        ser.write(("U1"+eol_char).encode('utf-8'))
        time.sleep(0.2)
        ans_v=sio.read()
        ansv=ans_v[ans_v.find(eol_char)+len(eol_char):ans_v.rfind(eol_char)]
        sys.stdout.write('Measured Voltage:'+str(ans_v))

        if ansv==0:
            break
        ### Measure current after volatage setting
        ser.write(("I1"+eol_char).encode('utf-8'))
        time.sleep(0.2)
        ans_i=sio.read()
        sys.stdout.write('Measured Current:'+str(ans_i))
        ansi=ans_i[ans_i.find(eol_char)+len(eol_char):ans_i.rfind(eol_char)]
        #mindata.append(str(incre))
        #mindata.append(str(ans))
 
        xs.append(ansv)
        ys.append(ansi)
        ax.scatter(xs, ys, color="black")
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Voltage Vs Current curve')
        plt.xlabel('Voltage (Volt)')
        plt.ylabel('Current (A)') 
        plt.pause(0.2)
        plt.draw() 
        mindata.append(str(ansv))
        mindata.append(str(ansi))
   
        finaloutput.append(mindata)
    

    print('\nDone\n')


    current_datetime = datetime.now()
    date = datetime.now().strftime('%Y%m%d')
    time_1 = datetime.now().strftime('-%H-%M-%S')
    filenames="HV_text-"+date+time_1+".txt"
    filenames_2="HV_text-"+date+time_1
    with open(filenames, 'w') as f:
        csv.writer(f, delimiter=' ').writerows(finaloutput)

    plt.savefig(filenames_2+".png")
    ser.close()  

    #Turn on if you want plot to stay in display after the test
    #while True:
    #	    time.sleep(0.2)





Vi = tkinter.Label(top, text = "V_start").place(x = 30,y = 50)  
  
Vf = tkinter.Label(top, text = "V_end").place(x = 30, y = 90)  
  
step = tkinter.Label(top, text = "V_step").place(x = 30, y = 130)  
  
  
en1=tkinter.Entry(top)
en1.place(x = 80, y = 50)  
en2=tkinter.Entry(top)  
en2.place(x = 80, y = 90)  
en3=tkinter.Entry(top)  
en3.place(x = 95, y = 130)  
 


starttest = tkinter.Button(top, text = "Start Test",activebackground = "pink", activeforeground = "blue",command=runTest)
starttest.place(x = 30, y = 170)  

top.mainloop()  
