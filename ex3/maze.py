import tkinter as tk
import tkinter.messagebox as tkm

class Application(tk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()