####Authors:
####Aloke Kumar Das, Chandiprasad Kar ############
####email "das21aloke@gmail.com"
# !/usr/bin/python3  




import tkinter
from tkinter import * 
import os 
  
top = Tk() 
top.title("HV test in I-Seg") 
  
top.geometry("400x250")  

def runTest():
	os.system("python3 run_HV_test.py -p %s -s %s -e %s"%(en1.get(),en2.get(),en3.get())) 

Vi = tkinter.Label(top, text = "V_start").place(x = 30,y = 50)    
Vf = tkinter.Label(top, text = "V_end").place(x = 30, y = 90)    
step = tkinter.Label(top, text = "V_step").place(x = 30, y = 130)  
  
  
en1=tkinter.Entry(top)
en1.place(x = 80, y = 50)  
en2=tkinter.Entry(top)  
en2.place(x = 80, y = 90)  
en3=tkinter.Entry(top)  
en3.place(x = 80, y = 130)  

Developername = tkinter.Label(top, text = "Developed by A. K. Das").place(x = 90,y = 230) 

starttest = tkinter.Button(top, text = "Start Test",activebackground = "pink", activeforeground = "blue",command=runTest)
starttest.place(x = 30, y = 170)  

top.mainloop()  
