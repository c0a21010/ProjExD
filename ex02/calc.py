from errno import ENETDOWN
import operator
import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm
import random as rd
from matplotlib.pyplot import axes

import numpy as np

my_operator = False
buttonlist = []

def printwindow():
    tkm.showwarning("おしたな","おしたな")


def clickbutton(event):
    btn = event.widget
    txt = btn["text"]
    my_operator = True
    entry.insert(tk.END,txt)

def operaterbutton(event):
    btn = event.widget
    txt = btn["text"]
    if my_operater:
        entry.insert(tk.END,txt)
        my_operater = False

def equalbutton(event):
    formula = entry.get()
    # if formula[0] == "[":
    #     youso = []
    #     for i in list(formula):
    #         ennzannsi = ""
    #         num = ""
    #         if i=="[":
    #             youso.append(np.array([]))
    #         elif i==",":
    #             youso[-1] = np.append(youso[-1],int(num))
    #         elif 48<=ord(i)<58:
    #             num += i
    #         elif i=="+":
    #             ennzannsi="+"
    #         elif i=="*":
    #             ennzannsi="*"
    #     print(youso)
    #     nps = np.array([])
    #     for i in youso:
    #         nps = np.append(nps,i,axis=0)
    #     ans = np.sum(nps,axis=0)
    # else:
    ans = eval(formula)
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(ans))

def deletebutton(event):
    entry.delete(0,tk.END)

def clearbutton(event):
    length = len(str(entry.get()))
    entry.delete(length-1)

def saikoro(event):
    entry.insert(tk.END,str(rd.randint(1,6)))

def add_button(arg_win,arg_text,bind_func,arg_row,arg_column):
    buttonlist.append(
            tk.Button(
                arg_win
                ,text=arg_text
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                )
        )
    buttonlist[-1].bind("<1>",bind_func)
    # buttonlist[-1].grid(row=(i//3)+1,column=i%3)
    buttonlist[-1].grid(row=arg_row,column=arg_column)
    
    
    

root = tk.Tk()
root.geometry("600x600")

entry = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan = 3)

numlist = [i for i in range(9,-1,-1)]
for i in range(10):
    add_button(root,numlist[i],clickbutton,(i//3)+1,i%3)

add_button(root,"+",clickbutton,0,3)
add_button(root,"-",clickbutton,1,3)
add_button(root,"*",clickbutton,2,3)
add_button(root,"/",clickbutton,3,3)
add_button(root,"=",equalbutton,4,3)
add_button(root,"AC",deletebutton,4,1)
add_button(root,"C",clearbutton,4,2)
add_button(root,"賽",saikoro,0,4)
# add_button(root,"[",clickbutton,1,4)
# add_button(root,"]",clickbutton,3,4)
# add_button(root,",",clickbutton,2,4)


root.mainloop()