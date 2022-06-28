import tkinter as tk
import tkinter.messagebox as tkm

from matplotlib import widgets

class Application(tk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)

        self.master.geometry()


        canvas = tk.Canvas(
            self.master,
            width = 1500,
            height = 900,
            bg="black"
        )

        canvas.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()