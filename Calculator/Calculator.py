import tkinter as tk 
from tkinter import ttk 
from tkinter import font 
from tkinter import * 
from math import sin, cos, tan,e, log, log2, log10, asin, acos, atan
import math


class  Main:
	"""docstring for  Main"""
	def __init__(self, root, fmt):
		self.root = root
		self.fmt = fmt 

	def design(self):
		self.input_area = tk.Entry(root, font=self.fmt, bg='grey',
		 fg='black', bd=3, justify=RIGHT)
		self.input_area.pack(ipady=10, fill=tk.X)

		frame = tk.Frame(root)

		self.fmt1 = font.Font(family='Calibri',size=12, weight='normal')

		s = ttk.Style()
		s.configure('Kim.TButton',bg='grey', foreground='black', font=self.fmt1,width=7)

		s1 = ttk.Style()
		s1.configure('Kim1.TButton', foreground='black', font=self.fmt1,width=15)

		t = (('1','2' ,'3','-'),('4','5','6','+')
			,('7','8','9','*'),('0','.','00','/'),
			('π', '2π','√', '%'),('x²','sin', 'cos','tan'),
			('π²','e²', '(',')'),
			('e','log','log2','log10'),('x³','sin⁻¹','cos⁻¹','tan⁻¹'))

		t1 = (('1','2' ,'3','-'),('4','5','6','+')
			,('7','8','9','*'),('0','.','00','/'),
			('π', '2π','√', '%'),('x²','sin', 'cos','tan'),
			('π²','e²', '(',')'),
			('e','log','log2','log10'),('x³','1/sin','1/cos','1/tan'))

		clear = ttk.Button(frame,text='Clear', style='Kim1.TButton',command=self.clear)
		clear.grid(row=1,column=0,columnspan=2)
		back = ttk.Button(frame,text='<-', style='Kim1.TButton', command=self.back)
		back.grid(row=1,column=2,columnspan=2)

		for x in range(9):
			for y in range(4):
				btn = ttk.Button(frame, text=t[x][y],style='Kim.TButton')
				btn.configure(command=lambda te=t1[x][y]: self.getText(te))
				btn.grid(row=x+2, column=y)

		exit = tk.Button(frame,text='Exit',font=self.fmt1,bg='red',fg='white',width=15, command=root.destroy)
		exit.grid(row=11,column=0,columnspan=2)
		equal = tk.Button(frame,text='=',font=self.fmt1,bg='green',fg='white',width=15, command=self.evaluate)
		equal.grid(row=11,column=2,columnspan=2)
		frame.pack()

	def clear(self):
		self.input_area.delete(0,len(self.input_area.get()))

	def back(self):
		self.input_area.delete(len(self.input_area.get())-1)

	def getText(self, te):
		if te == 'x²':
			v = self.input_area.get()
			value = math.pow(float(self.input_area.get()),2)
			self.clear()
			self.input_area.insert(0,f'({v})² = {value}')
		elif te == 'π':
			value = math.pi 
			self.clear()
			self.input_area.insert(0,value)
		elif te == '2π':
			value = 2 * math.pi
			self.clear()
			self.input_area.insert(0,value)
		elif te == '√':
			v = self.input_area.get()
			value = math.sqrt(float(self.input_area.get()))
			self.clear()
			self.input_area.insert(0, f'√{v} ={value}')
		elif te == 'π²':
			value = math.pi ** 2 
			self.clear()
			self.input_area.insert(0,value)
		elif te == 'e²':
			value = math.pow(math.e, float(self.input_area.get()))
			self.clear()
			self.input_area.insert(0,value)
		elif te == 'x³':
			v = self.input_area.get()
			value = math.pow(float(self.input_area.get()),3)
			self.clear()
			self.input_area.insert(0,f'({v})³ = {value}')
		
		else:
			self.input_area.insert(len(self.input_area.get()),te)



	def evaluate(self):
		value = str(self.input_area.get())
		get = eval(value)
		self.clear()
		self.input_area.insert(0,get)


if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('270x370')
	root.title('Calculator')
	root.resizable(0, 0)
	fmt = font.Font(family='helvetica', size=14)
	m = Main(root, fmt)
	m.design()
	root.mainloop()

	
