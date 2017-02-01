# -*- coding: utf-8 -*-
from Tkinter import*
root = Tk()
root.geometry("240x145")
def prov1():
    a = en1.get()
    toch = 0
    if a != ""  and a!= "-" and a != "+" and a != ".":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lberr.config(text = "В A минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lberr.config(text = "В A плюс не там")
                        return False
                if a[i] == ".":
                    toch += 1
            else:
                lberr.config(text = "Я не умею считать буквы")
                return False
            if toch > 1:
                lberr.config(text = "В A много точек")
                return False
        return True
    else:
       lberr.config(text = "В A нету ничего")
def prov2():
    a = en2.get()
    toch = 0
    if a != "":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lberr.config(text = "В B минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lberr.config(text = "В B плюс не там")
                        return False
                if a[i] == ".":
                    toch += 1
            else:
                lberr.config(text = "Я не умею считать буквы")
                return False
            if toch > 1:
                lberr.config(text = "В B много точек")
                return False
        return True
    else:
       lberr.config(text = "В B нету ничего")

def prov3():
    a = en3.get()
    toch = 0
    if a != "":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lberr.config(text = "В C минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lberr.config(text = "В C плюс не там")
                        return False
                if a[i] == ".":
                    toch += 1
            else:
                lberr.config(text = "Я не умею считать буквы")
                return False
            if toch > 1:
                lberr.config(text = "В C много точек")
                return False
        return True
    else:
       lberr.config(text = "В C нету ничего")
def discr():
    D = (float(en2.get())**2)-(4*float(en1.get())*float(en3.get()))
    return D

def reshit():
    if prov1():
        if prov2():
            if prov3():
                D = discr()
                D = round(D, 4)
                if D >= 0:
                    x1 = (-1*float(en2.get())+(D**0.5))/(2*float(en1.get()))
                    x2 = (-1*float(en2.get())-(D**0.5))/(2*float(en1.get()))
                    lbx1.config(text="x1="+str(round(x1,4)))
                    lbx2.config(text="x2="+str(round(x2,4)))
                    lbdisc.config(text="Дискриминант:"+str(D))
                else:
                    lberr.config(text="Дискриминант меньше 0")
                    lbx1.config(text="x1єØ")
                    lbx2.config(text="x2єØ")
                    lbdisc.config(text="Дискриминант:"+str(D))

labmain = Label(root, width=11, height=1, text="Ax^2+Bx+C=0", cursor="heart")
lb1 = Label(root, width=3, height=1, text="A=", cursor="heart")
lb2 = Label(root, width=3, height=1, text="B=", cursor="heart")
lb3 = Label(root, width=3, height=1, text="C=", cursor="heart")
lberr = Label(root, width=20, height=1, cursor="heart")
lbx1 = Label(root, width=8, height=1, cursor="heart")
lbx2 = Label(root, width=8, height=1, cursor="heart")
lbdisc = Label(root, width=15, height=1, cursor="heart")
en1 = Entry(root, width=7, cursor="heart")
en2 = Entry(root, width=7, cursor="heart")
en3 = Entry(root, width=7, cursor="heart")
doit = Button(root,text="Решить", width=5, height=2, command=reshit, cursor="heart")

labmain.place(x=5,y=0)
lb1.place(x=0, y=30)
lb2.place(x=0, y=50)
lb3.place(x=0, y=70)
lbx1.place(x=70, y=53)
lbx2.place(x=70, y=83)
en1.place(x=20, y=33)
en2.place(x=20, y=53)
en3.place(x=20, y=73)
lberr.place(x=70, y=33)
lbdisc.place(x=70, y=113)
doit.place(x=10, y=103)

root.mainloop()
