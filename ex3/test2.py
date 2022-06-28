import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    tmr = tmr + 1
    label["text"] = tmr
    jid = root.after(1000,count_up)

def button_click(event):
    btn=event.widget
    txt=btn["text"]

def key_down(event):
    key = event.keysym
    global jid

    if jid != None:

        root.after_cancel(jid)

        jid=None

        return
    
    # tkm.showinfo("Pushed a key.",f"{key}key was pushed.")
    jid = root.after(1000,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(
        root,
        font = ("TImes New Roman", 80))

    label.pack()

    # button = tk.Button(root,text="Don't Push!",command=button_click)
    # button.pack()

    root.bind("<KeyPress>",key_down)
    tmr = 0
    jid = None
    root.mainloop()