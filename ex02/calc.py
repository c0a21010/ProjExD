import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

def printwindow():
    tkm.showwarning("おしたな","おしたな")
def clickbutton(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END,txt)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan = 3)

numlist = [i for i in range(9,-1,-1)]

buttonlist = []
for i in range(10):
    buttonlist.append(
        tk.Button(
            root
            ,text=f"{numlist[i]}"
            ,width=4
            ,height=2
            ,font=("Times New Roman",30)
            )
    )
    buttonlist[len(buttonlist)-1].bind("<1>",clickbutton)
    buttonlist[len(buttonlist)-1].grid(row=(i//3)+1,column=i%3)

root.mainloop()