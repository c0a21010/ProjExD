import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

def printwindow():
    tkm.showwarning("おしたな","おしたな")

root = tk.Tk()
root.geometry("300x500")

buttonlist = []
for i in range(3):
    for j in range(3):
        buttonlist.append(
            tk.Button(
                root
                ,text=f"{9-(i*3+j)}"
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                ,command=printwindow
                )
        )
        buttonlist[len(buttonlist)-1].grid(row=i,column=j)

buttonlist.append(
            tk.Button(
                root
                ,text=f"{10}"
                ,width=4
                ,height=2
                ,font=("Times New Roman",30)
                ,command=printwindow
                )
        )
buttonlist[len(buttonlist)-1].grid(row=3,column=0)


root.mainloop()