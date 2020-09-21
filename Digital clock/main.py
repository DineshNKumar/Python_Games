from tkinter import *
from tkinter import ttk 
from tkinter import font 
import time 
import datetime

def quit(*args):
	root.destroy()

def clock():
	dt = datetime.datetime.now()
	dt = dt.strftime("%y/%m/%d, %H:%M:%S")

	txt.set(dt)

	root.after(1000, clock)

root = Tk()

root.attributes("-fullscreen", False)
root.configure(background='black')

root.bind("x", quit)
root.after(1000,clock)

fmt = font.Font(family='Consolas', size=80, weight='bold')
txt = StringVar()

lbl = ttk.Label(root, textvariable=txt, font=fmt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

