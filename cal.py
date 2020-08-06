from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("307x160")
root.config(bg='red')
root.title("Calculator-By-Suraj")
root.resizable(0,0)
root.iconbitmap("c.ico")
def bt1():
    text=btn1.cget("text")
    r.set(result.get()+text)
def bt2():
    text=btn2.cget("text")
    r.set(result.get()+text)
def bt3():
    text=btn3.cget("text")
    r.set(result.get()+text)

def bt5():
    text=btn5.cget("text")
    r.set(result.get()+text)
def bt6():
    text=btn6.cget("text")
    r.set(result.get()+text)
def bt4():
    text=btn4.cget("text")
    r.set(result.get()+text)
def btm():
    text=btnm.cget("text")
    r.set(result.get()+text)
def bt7():
    text=btn7.cget("text")
    r.set(result.get()+text)
def bt8():
    text=btn8.cget("text")
    r.set(result.get()+text)
def bt9():
    text=btn9.cget("text")
    r.set(result.get()+text)
def btmu():
    text=btnmmm.cget("text")
    r.set(result.get()+text)
def btr():
    p=eval(result.get())
    r.set(p)

def bt9():
    text=btn9.cget("text")
    r.set(result.get()+text)
def btd():
    text=btnd.cget("text")
    r.set(result.get()+text)
def btz():
    text=btnz.cget("text")
    r.set(result.get()+text)
def btc():
    r.set("")
    
def btpp():
    text=btnp.cget("text")
    r.set(result.get()+text)

def btplus():
    text=plus.cget("text")
    r.set(result.get()+text)
f=("arial",19,'bold')
r=StringVar()
result=Entry(root,font=f,textvariable=r,state='readonly')
result.pack(fill=X,)
f=Frame(root)
f.pack()
f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()
f3=Frame(root,)
f3.pack()
btn1=ttk.Button(f,text="1",command=bt1,)
btn1.grid(row=0,column=1)
btn2=ttk.Button(f,text="2",command=bt2)
btn2.grid(row=0,column=2)
btn3=ttk.Button(f,text="3",command=bt3)
btn3.grid(row=0,column=3)
plus=ttk.Button(f,text="+",command=btplus)
plus.grid(row=0,column=4)
btn4=ttk.Button(f1,text="4",command=bt4)
btn4.grid(row=1,column=1)
btn5=ttk.Button(f1,text="5",command=bt5)
btn5.grid(row=1,column=2)
btn6=ttk.Button(f1,text="6",command=bt6)
btn6.grid(row=1,column=3)
btnm=ttk.Button(f1,text="-",command=btm)
btnm.grid(row=1,column=4)
btn7=ttk.Button(f2,text="7",command=bt7)
btn7.grid(row=2,column=1)
btn8=ttk.Button(f2,text="8",command=bt8)
btn8.grid(row=2,column=2)
btn9=ttk.Button(f2,text="9",command=bt9)
btn9.grid(row=2,column=3)
btnmmm=ttk.Button(f2,text="*",command=btmu)
btnmmm.grid(row=2,column=4)
btnp=ttk.Button(f3,text='.',command=btpp)
btnp.grid(row=3,column=1)
btnz=ttk.Button(f3,text='0',command=btz)
btnz.grid(row=3,column=2)
btnd=ttk.Button(f3,text='/',command=btd)
btnd.grid(row=3,column=3)
btnc=ttk.Button(f3,text='c',command=btc)
btnc.grid(row=3,column=4)
btne=ttk.Button(text="=",command=btr)
btne.pack(fill=X)
root.mainloop()