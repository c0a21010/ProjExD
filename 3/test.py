from cProfile import label
import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.tmr = 0
        self.create_widets()

    def create_widets(self):

        self.label = tk.Label(
            self.root,
            font=("Times New Roman", 80)
        )

        self.label["text"] = self.tmr

        self.tmr = self.tmr + 1

        self.label.pack()

        self.after(1000,self.create_widets)

    def count_up(self):
        self.tmr = self.tmr+1
        # self.label["text"] = self.tmr
        self.label["text"] = self.tmr

        # self.after(1000,self.count_up)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

