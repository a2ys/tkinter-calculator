# -*- coding: utf- 8 -*-
# TODO: Out of digits prompt and add mannual entry of operations functionality

from tkinter import *
from tkinter import font as tkFont
import time

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title("CALCULATOR")
root.resizable(False, False)

segoe_font = tkFont.Font(family='Segoe UI', size=16)
segoe_font_ac = tkFont.Font(family='Segoe UI', size=8)

entry_text = StringVar()
inout = Entry(root, textvariable=entry_text)
inout.grid(row=0, column=0, columnspan=4, sticky="nsew")
operation = ''
spl_char = "~!@#$%^&*()_+`{}|[]\\:\";'<>?,/="

s = '⚠'
a = s.encode('utf-8')

num1 = 0
result = 0
operator = None

def clear():
    entry_text.set("")

def allclear():
    entry_text.set("")
    num1 = 0
    operator=""

def equals():
    global num1, operator

    try:
        tempvar = entry_text.get()
        num2 = float(tempvar)
        if operator == '/':
            if num2 != 0:
                answer = num1 / num2
                entry_text.set(answer)
                num1 = answer
                operator = None
            else:
                answer = a.decode()
                entry_text.set(answer)
                num1 = 0
                operator = None
        elif operator == '*':
            answer = num1 * num2
            entry_text.set(answer)
            num1 = answer
            operator = None
        elif operator == '-':
            answer = num1 - num2
            entry_text.set(answer)
            num1 = answer
            operator = None
        elif operator == '+':
            answer = num1 + num2
            entry_text.set(answer)
            num1 = answer
            operator = None

        tempvar2 = float(entry_text.get())
        if int(tempvar2) == tempvar2:
            entry_text.set(int(tempvar2))
        else:
            entry_text.set(round(tempvar2, 10))

    except ValueError:
        pass

def divide():
    global num1, operator

    try:
        tempvar = entry_text.get()
        num1 = float(tempvar)
        entry_text.set("")
        operator = '/'
    except ValueError:
        num1 = 0
        entry_text.set("")
        operator = '/'

def multiply():
    global num1, operator

    try:
        tempvar = entry_text.get()
        num1 = float(tempvar)
        entry_text.set("")
        operator = '*'
    except ValueError:
        num1 = 0
        entry_text.set("")
        operator = '/'

def minus():
    global num1, operator

    try:
        tempvar = entry_text.get()
        num1 = float(tempvar)
        entry_text.set("")
        operator = '-'
    except ValueError:
        num1 = 0
        entry_text.set("")
        operator = '-'

def plus():
    global num1, operator

    try:
        tempvar = entry_text.get()
        num1 = float(tempvar)
        entry_text.set("")
        operator = '+'
    except ValueError:
        num1 = 0
        entry_text.set("")
        operator = '+'

def tsev():
    entry_text.set(entry_text.get() + '7')

def teig():
    entry_text.set(entry_text.get() + '8')

def tnin():
    entry_text.set(entry_text.get() + '9')

def tfou():
    entry_text.set(entry_text.get() + '4')

def tfiv():
    entry_text.set(entry_text.get() + '5')

def tsix():
    entry_text.set(entry_text.get() + '6')

def tone():
    entry_text.set(entry_text.get() + '1')

def ttwo():
    entry_text.set(entry_text.get() + '2')

def tthr():
    entry_text.set(entry_text.get() + '3')

def tzer():
    entry_text.set(entry_text.get() + '0')

def decimal():
    variter = entry_text.get()

    if len(variter) == 0:
        entry_text.set('0.')
        return True

    for i in variter:
        if i == ".":
            entry_text.set(variter)
            break
        elif variter == a.decode():
            entry_text.set('0.')
        else:
            entry_text.set(variter + '.')

def character_limit_and_check_entered_value(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:20])

        for i in entry_text.get():
            if i.isalpha() or (i in spl_char):
                l = entry_text.get()
                dex = l.index(i)
                toset = l[:dex] + l[dex + 1:]
                entry_text.set(toset)

button18 = Button(root, text="AC", command=allclear, font=segoe_font_ac).grid(row=1, column=0, sticky="nsew")
button1 = Button(root, text="C", command=clear, font=segoe_font).grid(row=1, column=1, sticky="nsew")
button2 = Button(root, text="/", command=divide, font=segoe_font).grid(row=1, column=2, sticky="nsew")
button3 = Button(root, text="×", command=multiply, font=segoe_font).grid(row=1, column=3, sticky="nsew")
button5 = Button(root, text="7", command=tsev, font=segoe_font).grid(row=2, column=0, sticky="nsew")
button6 = Button(root, text="8", command=teig, font=segoe_font).grid(row=2, column=1, sticky="nsew")
button7 = Button(root, text="9", command=tnin, font=segoe_font).grid(row=2, column=2, sticky="nsew")
button4 = Button(root, text="-", command=minus, font=segoe_font).grid(row=2, column=3, sticky="nsew")
button9 = Button(root, text="4", command=tfou, font=segoe_font).grid(row=3, column=0, sticky="nsew")
button10 = Button(root, text="5", command=tfiv, font=segoe_font).grid(row=3, column=1, sticky="nsew")
button11 = Button(root, text="6", command=tsix, font=segoe_font).grid(row=3, column=2, sticky="nsew")
button8 = Button(root, text="+", command=plus, font=segoe_font).grid(row=3, column=3, sticky="nsew")
button12 = Button(root, text="1", command=tone, font=segoe_font).grid(row=4, column=0, sticky="nsew")
button13 = Button(root, text="2", command=ttwo, font=segoe_font).grid(row=4, column=1, sticky="nsew")
button14 = Button(root, text="3", command=tthr, font=segoe_font).grid(row=4, column=2, sticky="nsew")
button15 = Button(root, text="=", command=equals, font=segoe_font).grid(row=4, column=3, rowspan=2, sticky="nsew")
button16 = Button(root, text="0", command=tzer, font=segoe_font).grid(row=5, column=0, columnspan=2, sticky="nsew")
button17 = Button(root, text=".", command=decimal, font=segoe_font).grid(row=5, column=2, sticky="nsew")

entry_text.trace("w", lambda *args: character_limit_and_check_entered_value(entry_text))
root.mainloop()
