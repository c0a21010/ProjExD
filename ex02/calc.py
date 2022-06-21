import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

def printwindow():
    tkm.showwarning("おしたな","おしたな")

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
entry.insert(tk.END,"fugapiyo")
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
            ,command=printwindow
            )
    )
    buttonlist[len(buttonlist)-1].grid(row=(i//3)+1,column=i%3)

root.mainloop()