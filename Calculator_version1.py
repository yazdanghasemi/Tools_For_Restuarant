
import tkinter as tk
from tkinter import *


win = tk.Tk()
win.geometry('')
win.title('.:.Calculator.:.')
win.geometry('400x600+550+100')
win.resizable(0, 0)

screentxt = ''


def my_btndot():
    global screentxt
    screentxt += str('.')
    lbl.config(text=screentxt)


def my_btn0():
    global screentxt
    screentxt += str(0)
    lbl.config(text=screentxt)


def my_btn1():
    global screentxt
    screentxt += str(1)
    lbl.config(text=screentxt)


def my_btn2():
    global screentxt
    screentxt += str(2)
    lbl.config(text=screentxt)


def my_btn3():
    global screentxt
    screentxt += str(3)
    lbl.config(text=screentxt)


def my_btn4():
    global screentxt
    screentxt += str(4)
    lbl.config(text=screentxt)


def my_btn5():
    global screentxt
    screentxt += str(5)
    lbl.config(text=screentxt)


def my_btn6():
    global screentxt
    screentxt += str(6)
    lbl.config(text=screentxt)


def my_btn7():
    global screentxt
    screentxt += str(7)
    lbl.config(text=screentxt)


def my_btn8():
    global screentxt
    screentxt += str(8)
    lbl.config(text=screentxt)


def my_btn9():
    global screentxt
    screentxt += str(9)
    lbl.config(text=screentxt)


def my_btnclear():
    global lbl
    global screentxt
    screentxt = ''
    lbl.config(text=screentxt)


def my_btnadd():
    global screentxt
    screentxt += str('+')
    lbl.config(text=screentxt)


def my_btnminus():
    global screentxt
    screentxt += str('-')
    lbl.config(text=screentxt)


def my_btndivide():
    global screentxt
    screentxt += str('/')
    lbl.config(text=screentxt)


def my_btnmulti():
    global screentxt
    screentxt += str('*')
    lbl.config(text=screentxt)


def my_btnback():
    global screentxt
    if len(screentxt)>0:
        txtlist = list(screentxt)
        txtlist.remove(txtlist[-1])
        screentxt = ''.join(txtlist)
        lbl.config(text=screentxt)


def my_btnEqual():
    global screentxt
    screentxt = str(eval(screentxt))
    lbl.config(text=screentxt)


lbl = tk.Label(win, bg='#B22222', fg='#FFD700', font=10)
lbl.place(height=100, width=400, x=0, y=0)
btn0 = tk.Button(win, text='0', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn0)
btn0.place(height=100, width=200, x=0, y=500)
btn1 = tk.Button(win, text='1', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn1)
btn1.place(height=100, width=100, x=0, y=400)
btn2 = tk.Button(win, text='2', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn2)
btn2.place(height=100, width=100, x=100, y=400)
btn3 = tk.Button(win, text='3', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn3)
btn3.place(height=100, width=100, x=200, y=400)
btn4 = tk.Button(win, text='4', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn4)
btn4.place(height=100, width=100, x=0, y=300)
btn5 = tk.Button(win, text='5', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn5)
btn5.place(height=100, width=100, x=100, y=300)
btn6 = tk.Button(win, text='6', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn6)
btn6.place(height=100, width=100, x=200, y=300)
btn7 = tk.Button(win, text='7', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn7)
btn7.place(height=100, width=100, x=0, y=200)
btn8 = tk.Button(win, text='8', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn8)
btn8.place(height=100, width=100, x=100, y=200)
btn9 = tk.Button(win, text='9', bg='#2F4F4F',
                 fg='#FFD700', font=5, command=my_btn9)
btn9.place(height=100, width=100, x=200, y=200)
btnclear = tk.Button(win, text='C', bg='#2F4F4F',
                     fg='#FFD700', font=5, command=my_btnclear)
btnclear.place(height=100, width=200, x=0, y=100)
btnback = tk.Button(win, text=u'\u232B', bg='#2F4F4F',
                    fg='#FFD700', font=5, command=my_btnback)
btnback.place(height=100, width=100, x=200, y=100)
btnEqual = tk.Button(win, text='=', bg='#2F4F4F',
                     fg='#FFD700', font=5, command=my_btnEqual)
btnEqual.place(height=100, width=100, x=300, y=500)
btndot = tk.Button(win, text='.', bg='#2F4F4F',
                   fg='#FFD700', font=5, command=my_btndot)
btndot.place(height=100, width=100, x=200, y=500)
btndivide = tk.Button(win, text='÷', bg='#2F4F4F',
                      fg='#FFD700', font=5, command=my_btndivide)
btndivide.place(height=100, width=100, x=300, y=400)
btnmulti = tk.Button(win, text='x', bg='#2F4F4F',
                     fg='#FFD700', font=5, command=my_btnmulti)
btnmulti.place(height=100, width=100, x=300, y=300)
btnadd = tk.Button(win, text='+', bg='#2F4F4F',
                   fg='#FFD700', font=5, command=my_btnadd)
btnadd.place(height=100, width=100, x=300, y=200)
btnminus = tk.Button(win, text='-', bg='#2F4F4F',
                     fg='#FFD700', font=5, command=my_btnminus)
btnminus.place(height=100, width=100, x=300, y=100)


win.mainloop()
