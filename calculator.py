from tkinter import *
from tkinter import ttk
from tkinter import messagebox


cal = Tk()
cal.title('Calculator')

# logic calculator

def calc(key):
    global memory
    if key =='=':
        strl= '-+0123456789.*/()'
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, 'Введите число!')
            messagebox.showerror('Ошибка! ВВедите число!')
        
        try:
            res = eval(calc_entry.get())
            calc_entry.insert(END, '='+str(res))
        except:
            calc_entry.insert(END, 'ERROR! :(')
            messagebox.showerror('Ошибка! ВВедите число! :) ')
    elif key == 'C':
        calc_entry.delete(0, END)
    
    elif key == '+/-':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
               calc_entry.delete(0, '-')
        except IndexError:
            pass
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# created button

btn_list = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '=', 'C', '/',
    '.', '+/-', '(', ')'
]

r = 1
c = 0

for i in btn_list:
    res = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(cal, text=i, command=cmd ).grid(row=r, column=c)
    c += 1
    if c > 3:
        c=0
        r+=1
calc_entry = Entry(cal, width=40)
calc_entry.grid(row=0, column=0, columnspan=5)

cal.mainloop()

