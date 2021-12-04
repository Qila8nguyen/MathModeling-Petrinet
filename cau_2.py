from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
from typing import Sized, Text
import tkinter
import time
top = tkinter.Tk()
top.title("The patient's petri net")
frame=tkinter.Frame(top, highlightbackground="#D7DADA", highlightthickness=10,  height=430, width=850,bd=0 )
C = tkinter.Canvas(frame, bg="#D5edf7", height=430, width=850)
frame.pack()
C.pack()
wait=C.create_oval(100,90,160,150, outline="black", fill="white",width=2)
inside=C.create_oval(380,90,440,150, outline="black", fill="white",width=2)
done=C.create_oval(670,90,730,150, outline="black", fill="white",width=2)
arrow=C.create_line(160,120,240,120, fill="black",arrow='last', width=2)
arrow=C.create_line(270,120,380,120, fill="black",arrow='last', width=2)
arrow=C.create_line(440,120,520,120, fill="black",arrow='last', width=2)
arrow=C.create_line(590,120,670,120, fill="black",arrow='last', width=2)

wait_lable=tkinter.Label(C,text="wait",font=("arial", 14),bg="#D5edf7" ).place(x=110,y=55)
inside_lable=tkinter.Label(C,text="inside",font=("arial", 14),bg="#D5edf7" ).place(x=385,y=55)
done_lable=tkinter.Label(C,text="done",font=("arial", 14),bg="#D5edf7" ).place(x=675,y=55)
token_wait=tkinter.StringVar()
token_inside=tkinter.StringVar()
token_done=tkinter.StringVar()
lable=tkinter.Label(C,text="Enter the number of tokens in each place:",font=("arial", 14, "italic"),bg="#D5edf7" ).place(x=100,y=230)
lable=tkinter.Label(C,text="wait:",font=("arial", 14),bg="#D5edf7" ).place(x=100,y=280)
lable=tkinter.Label(C,text="inside:",font=("arial", 14),bg="#D5edf7" ).place(x=200,y=280)
lable=tkinter.Label(C,text="done:",font=("arial", 14),bg="#D5edf7" ).place(x=320,y=280)
data1=IntVar()
data2=IntVar()
data3=IntVar()
entryFree=tkinter.Entry(C,textvariable=data1, font=("arial", 13),bg="white",width=4,justify="right").place(x=150,y=280)
entryBusy=tkinter.Entry(C,textvariable=data2,font=("arial", 13),bg="white",width=4,justify="right").place(x=265,y=280)
entryDocu=tkinter.Entry(C,textvariable=data3,font=("arial", 13),bg="white",width=4,justify="right").place(x=377,y=280)

w=0
i=0
d=0
def Enter():
    global w,i,d
    w=data1.get()
    i=data2.get()
    d=data3.get()
    getToken()  
enter=tkinter.Button(C,text="Enter",font=("arial",13,"bold"),bg="white", command=Enter,width=6,height=1).place(x=450,y=270)    
def getToken():
    token_wait.set(str(w))
    wait=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=token_wait,width=4 ).place(x=112,y=110)
    token_inside.set(str(i))
    inside=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=token_inside,width=4 ).place(x=392,y=110)
    token_done.set(str(d))
    done=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=token_done,width=4 ).place(x=682,y=110)
def click_start():
    global w,i
    if w>0:
        w-=1
        token_wait.set(str(w))
        token_x=160
        token_y=120
        token = C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
        for _ in range(26):
            right(token)
            C.update() 
            time.sleep(0.05)
        i+=1
        token_inside.set(str(i))
        C.delete(token)
start=tkinter.Button(C,text="start",font=("arial",13,"bold"),bg="white",command=click_start,width=5,height=2).place(x=240,y=95)
def click_change():
    global i,d
    if i>0:
        i-=1
        token_inside.set(str(i))
        token_x=440
        token_y=120
        token = C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
        for _ in range(28):
            right(token)
            C.update() 
            time.sleep(0.05)
        d+=1
        token_done.set(str(d))
        C.delete(token)
change=tkinter.Button(C,text="change",font=("arial",13,"bold"),bg="white",command=click_change,width=6,height=2).place(x=520,y=95)
def right(token):
            x=8
            y=0
            C.move(token, x, y)
top.mainloop()

