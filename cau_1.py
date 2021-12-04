from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
from typing import Sized, Text
import tkinter
import time
top = tkinter.Tk()
top.title("The specialist's petri net")
frame=tkinter.Frame(top, highlightbackground="#D7DADA", highlightthickness=10,  height=500, width=550,bd=0 )
C = tkinter.Canvas(frame, bg="#D5edf7", height=500, width=550)
frame.pack()
C.pack()
free=C.create_oval(100,60,160,120, outline="black", fill="white",width=2)
busy=C.create_oval(240,190,300,250, outline="black", fill="white",width=2)
docu=C.create_oval(380,60,440,120, outline="black", fill="white",width=2)
       #mui ten
arrow=C.create_line(130,120,130,195, fill="black",arrow='last', width=2)
arrow=C.create_line(160,220,240,220, fill="black",arrow='last', width=2)
arrow=C.create_line(300,220,375,220, fill="black",arrow='last', width=2)
arrow=C.create_line(410,200,410,120, fill="black",arrow='last', width=2)
arrow=C.create_line(380,90,300,90, fill="black",arrow='last', width=2)
arrow=C.create_line(240,90,160,90, fill="black",arrow='last', width=2)
free_lable=tkinter.Label(C,text="free",font=("arial", 14),bg="#D5edf7" ).place(x=110,y=25)
busy_lable=tkinter.Label(C,text="busy",font=("arial", 14),bg="#D5edf7" ).place(x=250,y=155)
docu_lable=tkinter.Label(C,text="docu",font=("arial", 14),bg="#D5edf7" ).place(x=390,y=25)
lable=tkinter.Label(C,text="Enter the number of tokens in each place:",font=("arial", 14, "italic"),bg="#D5edf7" ).place(x=50,y=330)
lable=tkinter.Label(C,text="free:",font=("arial", 14),bg="#D5edf7" ).place(x=50,y=380)
lable=tkinter.Label(C,text="busy:",font=("arial", 14),bg="#D5edf7" ).place(x=150,y=380)
lable=tkinter.Label(C,text="docu:",font=("arial", 14),bg="#D5edf7" ).place(x=250,y=380)
data1=IntVar()
data2=IntVar()
data3=IntVar()
entryFree=tkinter.Entry(C,textvariable=data1, font=("arial", 13),bg="white",width=4,justify="right").place(x=100,y=380)
entryBusy=tkinter.Entry(C,textvariable=data2,font=("arial", 13),bg="white",width=4,justify="right").place(x=207,y=380)
entryDocu=tkinter.Entry(C,textvariable=data3,font=("arial", 13),bg="white",width=4,justify="right").place(x=307,y=380)
f=4
b=4
d=4
def Enter():
    global f,b,d
    f=data1.get()
    b=data2.get()
    d=data3.get()
    getToken()  
enter=tkinter.Button(C,text="Enter",font=("arial",13,"bold"),bg="white", command=Enter,width=6,height=1).place(x=380,y=370)
fe=tkinter.StringVar()
bu=tkinter.StringVar()
do=tkinter.StringVar()
def getToken():
    fe.set(str(f))
    free=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=fe,width=4).place(x=112,y=80)
    bu.set(str(b))
    busy=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=bu,width=4).place(x=252,y=210)
    do.set(str(d))
    docu=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=do,width=4).place(x=392,y=80)
def click_start():
  global f,b
  if f>0:   
    f-=1
    fe.set(str(f))
    token_x=130
    token_y=120
    token = C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
    for _ in range(20):
        down(token)
        C.update() 
        time.sleep(0.03)
    for _ in range(20):
        right(token)
        C.update() 
        time.sleep(0.03)
    b+=1
    bu.set(str(b))
    C.delete(token)
start=tkinter.Button(C,text="start",font=("arial",13,"bold"),bg="white",command=click_start,width=5,height=2).place(x=100,y=195)   
def click_change():
  global b,d
  if b>0:
    b-=1
    bu.set(str(b))
    token_x=300
    token_y=220
    token = C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
    for _ in range(22):
        right(token)
        C.update() 
        time.sleep(0.03)
    for _ in range(20):
        up(token)
        C.update() 
        time.sleep(0.03)
    d+=1
    do.set(str(d))
    C.delete(token)
change=tkinter.Button(C,text="change",font=("arial",13,"bold"),bg="white",command=click_change,width=6,height=2).place(x=375,y=195)   
def click_end():
  global d,f
  if d>0:
    d-=1
    do.set(str(d))
    token_x=380
    token_y=90
    token = C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
    for _ in range(20):
        left(token)
        C.update() 
        time.sleep(0.03)
    for _ in range(20):
        left(token)
        C.update() 
        time.sleep(0.03) 
    f+=1
    fe.set(str(f))
    C.delete(token)
end=tkinter.Button(C,text="end",font=("arial",13,"bold"),bg="white",command=click_end,width=5,height=2).place(x=240,y=65)   
def left(token):
            x=-5
            y=0
            C.move(token, x, y)

def right(token):
            x=5
            y=0
            C.move(token, x, y)
def up(token):
            x=0
            y=-5
            C.move(token, x, y)
def down(token):
            x=0
            y=5
            C.move(token, x, y)


top.mainloop()