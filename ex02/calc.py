import operator
import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

my_operator = False

def printwindow():
    tkm.showwarning("おしたな","おしたな")


def clickbutton(event):
    btn = event.widget
    txt = btn["text"]
    my_operator = False
    entry.insert(tk.END,txt)

def operaterbutton(event):
    btn = event.widget
    txt = btn["text"]
    if not(my_operater):
        entry.insert(tk.END,txt)
        my_operater = True

def equalbutton(event):
    formula = entry.get()
    ans = eval(formula)
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(ans))
    
    

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan = 3)

numlist = [i for i in range(9,-1,-1)]

buttonlist = []
for i in range(12):
    if i<10:
        buttonlist.append(
            tk.Button(
                root
                ,text=f"{numlist[i]}"
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                )
        )
        buttonlist[-1].bind("<1>",clickbutton)
    elif i==10:
        buttonlist.append(
            tk.Button(
                root
                ,text="+"
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                )
        )
        buttonlist[-1].bind("<1>",clickbutton)
    elif i==11:
        buttonlist.append(
            tk.Button(
                root
                ,text="="
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                )
        )
        buttonlist[-1].bind("<1>",equalbutton)
    buttonlist[-1].grid(row=(i//3)+1,column=i%3)

root.mainloop()