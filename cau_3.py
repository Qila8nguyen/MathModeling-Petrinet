from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
from typing import Sized, Text
import tkinter
import time
top = tkinter.Tk()
top.title("Clinic petri net")
frame=tkinter.Frame(top, highlightbackground="#D7DADA", highlightthickness=10,  height=600, width=850,bd=0 )
C = tkinter.Canvas(frame, bg="#D5edf7", height=600, width=850)
frame.pack()
C.pack()

wait=C.create_oval(110,190,170,250, outline="black", fill="white",width=2)
inside=C.create_oval(380,190,440,250, outline="black", fill="white",width=2)
done=C.create_oval(660,190,720,250, outline="black", fill="white",width=2)
free=C.create_oval(245,70,305,130, outline="black", fill="white",width=2)
docu=C.create_oval(525,70,585,130, outline="black", fill="white",width=2)
busy=C.create_oval(380,310,440,370, outline="black", fill="white",width=2)

arrow=C.create_line(275,130,275,195, fill="black",arrow='last', width=2)
arrow=C.create_line(275,245,275,340,380,340, fill="black",arrow='last', width=2)
arrow=C.create_line(440,340,555,340,555,245 ,fill="black",arrow='last', width=2)
arrow=C.create_line(170,220,240,220, fill="black",arrow='last', width=2)
arrow=C.create_line(270,220,380,220, fill="black",arrow='last', width=2)
arrow=C.create_line(440,220,520,220, fill="black",arrow='last', width=2)
arrow=C.create_line(590,220,660,220, fill="black",arrow='last', width=2)
arrow=C.create_line(555,195,555,130, fill="black",arrow='last', width=2)
arrow=C.create_line(525,100,445,100, fill="black",arrow='last', width=2)
arrow=C.create_line(395,100,305,100, fill="black",arrow='last', width=2)


wait_lable=tkinter.Label(C,text="wait",font=("arial", 14),bg="#D5edf7" ).place(x=120,y=160)
busy_lable=tkinter.Label(C,text="busy",font=("arial", 14),bg="#D5edf7" ).place(x=390,y=280)
inside_lable=tkinter.Label(C,text="inside",font=("arial", 14),bg="#D5edf7" ).place(x=385,y=160)
docu_lable=tkinter.Label(C,text="docu",font=("arial", 14),bg="#D5edf7" ).place(x=530,y=40)
free_lable=tkinter.Label(C,text="free",font=("arial", 14),bg="#D5edf7" ).place(x=255,y=40)
done_lable=tkinter.Label(C,text="done",font=("arial", 14),bg="#D5edf7" ).place(x=665,y=160)

wa=tkinter.StringVar()
ins=tkinter.StringVar()
bu=tkinter.StringVar()
doc=tkinter.StringVar()
don=tkinter.StringVar()
fe=tkinter.StringVar()

lable=tkinter.Label(C,text="Enter the number of tokens in each place:",font=("arial", 15, "italic"),bg="#D5edf7" ).place(x=50,y=430)
lable=tkinter.Label(C,text="wait:",font=("arial", 15),bg="#D5edf7" ).place(x=50,y=480)
lable=tkinter.Label(C,text="inside:",font=("arial", 15),bg="#D5edf7" ).place(x=155,y=480)
lable=tkinter.Label(C,text="busy:",font=("arial", 15),bg="#D5edf7" ).place(x=275,y=480)
lable=tkinter.Label(C,text="done:",font=("arial", 15),bg="#D5edf7" ).place(x=380,y=480)
lable=tkinter.Label(C,text="docu:",font=("arial", 15),bg="#D5edf7" ).place(x=490,y=480)
lable=tkinter.Label(C,text="free:",font=("arial", 15),bg="#D5edf7" ).place(x=600,y=480)

data1=IntVar()
data2=IntVar()
data3=IntVar()
data4=IntVar()
data5=IntVar()
data6=IntVar()

entryWait=tkinter.Entry(C,textvariable=data1, font=("arial", 12),bg="white",width=4,justify="right").place(x=100,y=483)
entryInside=tkinter.Entry(C,textvariable=data2,font=("arial", 12),bg="white",width=4,justify="right").place(x=220,y=483)
entryBusy=tkinter.Entry(C,textvariable=data3,font=("arial", 12),bg="white",width=4,justify="right").place(x=330,y=483)
entryDone=tkinter.Entry(C,textvariable=data4, font=("arial", 12),bg="white",width=4,justify="right").place(x=437,y=483)
entryDocu=tkinter.Entry(C,textvariable=data5,font=("arial", 12),bg="white",width=4,justify="right").place(x=545,y=483)
entryFree=tkinter.Entry(C,textvariable=data6,font=("arial", 12),bg="white",width=4,justify="right").place(x=647,y=483)

w=0
b=0
i=0
done1=0
docu1=0
f=1
def Enter():
    global w,b,i,done1,docu1,f
    w=data1.get()
    i=data2.get()
    b=data3.get()
    done1=data4.get()
    docu1=data5.get()
    f=data6.get()
    getToken()
def getToken():    
    wa.set(str(w))
    wait=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=wa,width=4 ).place(x=122,y=210)
    bu.set(str(b))
    busy=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=bu,width=4 ).place(x=392,y=330)
    ins.set(str(i))
    inside=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=ins,width=4 ).place(x=392,y=210)
    doc.set(str(docu1))
    docu=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=doc,width=4 ).place(x=537,y=90)
    don.set(str(done1))
    done=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=don,width=4 ).place(x=672,y=210)
    fe.set(str(f))
    free=tkinter.Label(C,font=("arial", 10, 'bold'),bg="white",textvariable=fe,width=4 ).place(x=257,y=90)
enter=tkinter.Button(C,text="Enter",font=("arial",13,"bold"),bg="white", command=Enter,width=6,height=1).place(x=720,y=473)    
def click_start():
    global w,f,i,b
    if(f>0 and w>0):
        f-=1
        w-=1
        wa.set(str(w))
        fe.set(str(f))
        token_x_wait=170
        token_y_wait=220
        token_x_free=275
        token_y_free=130
        tokenwait=C.create_oval(token_x_wait-3,token_y_wait-3,token_x_wait+3,token_y_wait+3, outline="black", fill="black")
        tokenfree=C.create_oval(token_x_free-3,token_y_free-3,token_x_free+3,token_y_free+3, outline="black", fill="black")
        for _ in range(20):
            right(tokenwait)
            down(tokenfree)
            C.update()
            time.sleep(0.03)
        for _ in range(22):
            down(tokenfree)
            C.update()
            time.sleep(0.02)
        
        for _ in range(20):
            right(tokenwait)
            right(tokenfree)
            C.update()
            time.sleep(0.03)
        i+=1
        ins.set(str(i))
        b+=1
        bu.set(str(b))
        C.delete(tokenwait)
        C.delete(tokenfree)
start=tkinter.Button(C,text="start",font=("arial",13,"bold"),command=click_start,width=6,height=2).place(x=240,y=195)
def click_change():
    global i,b,done1,docu1
    if(i>0 and b>0):
        i-=1
        b-=1
        bu.set(str(b))
        ins.set(str(i))
        token_x_busy=440
        token_y_busy=340
        token_x_inside=440
        token_y_inside=220
        tokenbusy=C.create_oval(token_x_busy-3,token_y_busy-3,token_x_busy+3,token_y_busy+3, outline="black", fill="black")
        tokeninside=C.create_oval(token_x_inside-3,token_y_inside-3,token_x_inside+3,token_y_inside+3, outline="black", fill="black")
        for _ in range(23):
            right(tokeninside)
            
            right(tokenbusy)
            C.update()
            time.sleep(0.03)
        
        for _ in range(20):
            right(tokeninside)
            up(tokenbusy)
            C.update()
            time.sleep(0.05)
        done1+=1
        don.set(str(done1))
        docu1+=1
        doc.set(str(docu1))
        
        C.delete(tokeninside)
        C.delete(tokenbusy)
change=tkinter.Button(C,text="change",font=("arial",13,"bold"),command=click_change,width=6,height=2).place(x=520,y=195)
def click_end():
    global docu1,f
    if(docu1>0):
        docu1-=1
        doc.set(str(docu1))
        token_x=525
        token_y=100
        token=C.create_oval(token_x-3,token_y-3,token_x+3,token_y+3, outline="black", fill="black")
        for _ in range(54):
            left(token)
            C.update()
            time.sleep(0.03)
        f+=1
        fe.set(str(f))
        C.delete(token)
end=tkinter.Button(C,text="end",font=("arial",13,"bold"),command=click_end,width=6,height=2).place(x=375,y=75)
def left(token):
            x=-4
            y=0
            C.move(token, x, y)

def right(token):
            x=5
            y=0
            C.move(token, x, y)
def up(token):
            x=0
            y=-10.5
            C.move(token, x, y)
def down(token):
            x=0
            y=5
            C.move(token, x, y)
top.mainloop()