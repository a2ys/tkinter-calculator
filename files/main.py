# TODO: Add mannual entry of operations functionality

from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox, Toplevel
from PIL import ImageTk, Image

root = Tk()
root.geometry('700x600')
root.grid_rowconfigure((0,1,2,3,4,5), weight=1)
root.grid_columnconfigure((0,1,2,3), weight=1)
root.title("CALCULATOR")
root.resizable(False, False)

vartemp = StringVar()
vartemp.set('The source code is available on GitHub.\nPress the button below to copy the link.')
path = 'frame.png'
img = ImageTk.PhotoImage(Image.open(path))

menubar = Menu(root)

cfnt = tkFont.Font(family='Segoe UI', size=11)

def qclick():
    mb = messagebox.askyesno('QUITTING', 'Are you sure you want to quit the application?')

    if mb == True:
        root.quit()
    else:
        pass

def copylink():
    global vartemp

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append('https://github.com/AayushShukla2006/tkinter-calculator')
    r.update()
    r.destroy()

def gsc():
    global vartemp, img

    window = Toplevel(root)
    window.title('GET SOURCE CODE')
    window.geometry('350x450')
    window.resizable(False, False)
    window.grab_set()

    Label(window, textvariable=vartemp, font=cfnt).pack()
    bt = Button(window, text='Copy Link', command=copylink, font=cfnt)
    bt.pack()

    q = StringVar()
    q.set('or you can also scan the QR code below.')
    Label(window, textvariable=q, font=cfnt).pack()
    label = Label(window, image=img).pack(padx=10, pady=10)

def atp():
    messagebox.showinfo('ABOUT THE PROJECT', 'Hey, I\'m Aayush Shukla and this is a small project - \'Tkinter Calculator\'. I  gave it the basic functionalities every calculator software has (with some known issues mentioned in my GitHub). I started working on this project on 11th of November, 2021 and completed it on 20th of November, 2021. I am not currently maintaining the source code but it will always be freely available on GitHub as an open-source project and will be always open to your contributions.')

comwindow = Menu(menubar, tearoff=0)
comwindow.add_command(label="Quit", command=qclick)
menubar.add_cascade(label="Commands", menu=comwindow)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About the buttons")
helpmenu.add_command(label="About the project", command=atp)
helpmenu.add_separator()
helpmenu.add_command(label="Get source code", command=gsc)
menubar.add_cascade(label="About", menu=helpmenu)

segoe_font = tkFont.Font(family='Segoe UI', size=28)
segoe_font_ac = tkFont.Font(family='Segoe UI',weight='bold', size=28)

entry_text = StringVar()
inout = Entry(root, textvariable=entry_text, font=segoe_font)
inout.grid(row=0, column=0, columnspan=4, sticky="nsew")
operation = ''
spl_char = "~!@#$%^&*()_+`{}|[]\\:\";'<>?,/="

num1 = 0
result = 0
tempst = ''
operator = None

def clear():
    entry_text.set("")

def allclear():
    entry_text.set("")
    num1 = 0
    operator=""

def equals():
    global num1, operator, tempst

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
                entry_text.set('')
                messagebox.showerror('Division Error', 'Cannot divide by 0')
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

        tempvar2 = str(entry_text.get())
        if len(tempvar2) == 0:
            entry_text.set('')
        else:
            if int(float(tempvar2)) == float(tempvar2):
                if len(tempvar2) > 10:
                    entry_text.set('')
                    messagebox.showwarning('Out of digits', f'The answer cannot be printed as its length is greater than 10.\nAnswer is : {int(float(tempvar2))}')
                else:
                    entry_text.set(int(float(tempvar2)))
            else:
                entry_text.set(round(float(tempvar2), 5))
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
        for i in entry_text.get():
            if i.isalpha() or (i in spl_char):
                l = entry_text.get()
                dex = l.index(i)
                toset = l[:dex] + l[dex + 1:]
                entry_text.set(toset)

button18 = Button(root, text="AC", command=allclear, font=segoe_font_ac).grid(row=1, column=0, sticky="nsew")
button1 = Button(root, text="C", command=clear, font=segoe_font_ac).grid(row=1, column=1, sticky="nsew")
button2 = Button(root, text="/", command=divide, font=segoe_font_ac).grid(row=1, column=2, sticky="nsew")
button3 = Button(root, text="×", command=multiply, font=segoe_font).grid(row=1, column=3, sticky="nsew")
button5 = Button(root, text="7", command=tsev, font=segoe_font).grid(row=2, column=0, sticky="nsew")
button6 = Button(root, text="8", command=teig, font=segoe_font).grid(row=2, column=1, sticky="nsew")
button7 = Button(root, text="9", command=tnin, font=segoe_font).grid(row=2, column=2, sticky="nsew")
button4 = Button(root, text="-", command=minus, font=segoe_font_ac).grid(row=2, column=3, sticky="nsew")
button9 = Button(root, text="4", command=tfou, font=segoe_font).grid(row=3, column=0, sticky="nsew")
button10 = Button(root, text="5", command=tfiv, font=segoe_font).grid(row=3, column=1, sticky="nsew")
button11 = Button(root, text="6", command=tsix, font=segoe_font).grid(row=3, column=2, sticky="nsew")
button8 = Button(root, text="+", command=plus, font=segoe_font_ac).grid(row=3, column=3, sticky="nsew")
button12 = Button(root, text="1", command=tone, font=segoe_font).grid(row=4, column=0, sticky="nsew")
button13 = Button(root, text="2", command=ttwo, font=segoe_font).grid(row=4, column=1, sticky="nsew")
button14 = Button(root, text="3", command=tthr, font=segoe_font).grid(row=4, column=2, sticky="nsew")
button15 = Button(root, text="=", command=equals, font=segoe_font_ac).grid(row=4, column=3, rowspan=2, sticky="nsew")
button16 = Button(root, text="0", command=tzer, font=segoe_font).grid(row=5, column=0, columnspan=2, sticky="nsew")
button17 = Button(root, text=".", command=decimal, font=segoe_font_ac).grid(row=5, column=2, sticky="nsew")

entry_text.trace("w", lambda *args: character_limit_and_check_entered_value(entry_text))
root.config(menu=menubar)
root.mainloop()
