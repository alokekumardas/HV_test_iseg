####Authors:
####Aloke Kumar Das, Chandiprasad Kar ############
####email "das21aloke@gmail.com"
# !/usr/bin/python3  

import tkinter
from tkinter import * 
import os 
import webbrowser  
top = Tk() 
top.title("HV test in I-Seg") 
  
top.geometry("400x250") 
 
def callback():
        webbrowser.open_new(r"https://github.com/alokekumardas/HV_test_iseg/blob/main/README.md")

def runTest():
	#os.system(r'cd C:\Users\dell\Desktop\HV_test\HV_test_iseg')	
	#os.system("python3 run_HV_test.py -s %s -e %s -p %s"%(var1,var2,var3))
	os.system("python3 run_HV_test.py -s %s -e %s -p %s"%(en1.get(),en2.get(),en3.get()))

Vi = tkinter.Label(top, text = "V_start").place(x = 30,y = 50)    
Vf = tkinter.Label(top, text = "V_end").place(x = 30, y = 90)    
step = tkinter.Label(top, text = "V_step").place(x = 30, y = 130)  

link =tkinter.Button(top, text="Help", command=callback)
link.place(x=350, y=10)  
  
en1=tkinter.Entry(top)
en1.place(x = 80, y = 50)  
en2=tkinter.Entry(top)  
en2.place(x = 80, y = 90)  
en3=tkinter.Entry(top)  
en3.place(x = 80, y = 130)  
#var1=en1.get()
#var2=en2.get()
#var3=en3.get()

#if en1.get()=="" :
#	var1="10"
#if en2.get()=="" :
#	var2="100"
#if en3.get()=="" :
#	var3="10"


Developername = tkinter.Label(top, text = "Developed by A. K. Das").place(x = 90,y = 230) 
starttest = tkinter.Button(top, text = "Start Test",activebackground = "pink", activeforeground = "blue",command=runTest)
starttest.place(x = 30, y = 170)  

top.mainloop()  
