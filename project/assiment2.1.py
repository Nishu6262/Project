
from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())  +int(e5.get())
    c  =  myText.set(res)
    return c 


def get_gst():
    gst=(int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get()))*12/100
   
    d = mytext2.set(gst)
    return d



def get_st():
    st=(int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get()))*6/100
    r = mytext3.set(st)
    return r


def get_total():
    res=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())
    gst=(int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get()))*12/100
    st=(int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get()))*6/100
    
    total = res + gst + st
    f = mytext4.set(total)
    return f

master = Tk()
myText = StringVar();
mytext2=StringVar();
mytext3 =StringVar();
mytext4 = StringVar();
Label(master, text="First").grid(row=0, column=0)
Label(master, text="Second").grid(row=1, column=0)
Label(master, text="third").grid(row=2, column=0)
Label(master, text="fourth").grid(row=3, column=0)
Label(master, text="fifth").grid(row=4, column=0)

Label(master, text="Result:").grid(row=6, column=0)
result=Label(master, text="", textvariable=myText).grid(row=6,column=1)

Label(master, text="GST:").grid(row=8, column=0)
gst=Label(master, text="", textvariable=mytext2).grid(row=8,column=1)

Label(master, text="ST").grid(row=10, column=0)
st=Label(master, text="", textvariable=mytext3).grid(row=10,column=1)

Label(master, text="Total").grid(row=11, column=0)
st=Label(master, text="", textvariable=mytext4).grid(row=11,column=1)

 
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=0, column=2)

d = Button(master, text="GST", command=get_gst)
d.grid(row=1, column=2)

y = Button(master, text="ST", command=get_st)
y.grid(row=2, column=2)

z = Button(master, text="Total", command=get_total)
z.grid(row=3, column=2)


mainloop()