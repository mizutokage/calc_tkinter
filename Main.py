import math
import tkinter as tk

class Calculator(tk.Frame):
    #create window
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master.geometry('185x240')
        self.master.resizable(0,0)
        self.master.title('Calculator')
        self.entry = tk.Entry(self.master, justify='right')
        self.label = tk.Label(self.master, anchor='e', height=1, font=('',8), bg='white')
        self.creat_widgets()

    #input number
    def input(self, num):
        def n():
            self.entry.insert(tk.END, num)
        return n

    #four arithmetic operations
    def operations(self, ope):
        self.entry.insert(tk.END, ope)
        txt = self.entry.get()
        self.label.config(text=txt)

    #one-hundredth
    def one_hundredth(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, eval(txt + '/100'))

    #clearall
    def clear_all(self):
        self.entry.delete(0, tk.END)
        self.label.config(text='')

    #clearone
    def clear_one(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, txt[:-1])

    #square root
    def square(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, math.sqrt(float(txt)))
        self.label.config(text='sqrt(' + txt + ')')

    #equals
    def equals(self):
        txt = self.entry.get()
        self.value = eval(self.entry.get().replace('÷', '/').replace('×', '*').replace('＋', '+').replace('－', '-'))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.value)
        self.label.config(text=txt)

    #display part
    def creat_widgets(self):
        Buttons = [ 
        ['7', '8', '9'],
        ['4', '5', '6'], 
        ['1', '2', '3'], 
        ]
        for i, ro in enumerate(Buttons):
            for j, co in enumerate(ro):
                tk.Button(self.master, text=co, width=5, command=self.input(co)).grid(row=i+4, column=j)
        self.label.grid(row=0, column=0, columnspan=4, sticky='ew')
        self.entry.grid(row=1, column=0, columnspan=4, sticky='nsew')
        tk.Button(self.master, text='%', width=5, command=lambda: self.one_hundredth()).grid(row=2, column=0)
        tk.Button(self.master, text='CE', width=5, command=lambda: self.clear_all()).grid(row=2, column=1)
        tk.Button(self.master, text='⇦', width=5, command=lambda: self.clear_one()).grid(row=2, column=2, columnspan=2, sticky='ew')
        tk.Button(self.master, text='(', width=5, command=lambda: self.operations('(')).grid(row=3, column=0)
        tk.Button(self.master, text=')', width=5, command=lambda: self.operations(')')).grid(row=3, column=1)
        tk.Button(self.master, text='√', width=5, command=lambda: self.square()).grid(row=3, column=2)
        tk.Button(self.master, text='÷', width=5, command=lambda: self.operations('÷')).grid(row=3, column=3)
        tk.Button(self.master, text='×', width=5, command=lambda: self.operations('×')).grid(row=4, column=3)
        tk.Button(self.master, text='－', width=5, command=lambda: self.operations('－')).grid(row=5, column=3)
        tk.Button(self.master, text='＋', width=5, command=lambda: self.operations('＋')).grid(row=6, column=3)
        tk.Button(self.master, text='＝', width=5, command=lambda: self.equals()).grid(row=7, column=3)
        tk.Button(self.master, text='0', width=12, command=self.input('0')).grid(row=7, column=0, columnspan=2)
        tk.Button(self.master, text='.', width=5, command=self.input('.')).grid(row=7, column=2)

calc = Calculator(tk.Tk())
calc.mainloop()