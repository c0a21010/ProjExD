import tkinter as tk
import tkinter.messagebox as tkm

from matplotlib import image, widgets

class Application(tk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)

        self.master.geometry()

        # self.key = ""
        global key
        key = ""


        self.canvas = tk.Canvas(
            self.master,
            width = 1500,
            height = 900,
            bg="black"
        )

        self.kokaton = tk.PhotoImage(file="5.png")

        global cx, cy
        cx = 300
        cy = 400

        self.canvas.create_image(cx,cy,image=self.kokaton,tag="kokaton")

        self.canvas.pack()

        self.master.bind("<KeyPress>", self.key_down)

    def key_down(event):
        key = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()