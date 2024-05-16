from tkinter import StringVar, Label, Entry, IntVar


class TextWithLabel:
    def __init__(self, master, text, x, y, distance=60, disabled=False, width=20):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.distance = distance
        self.variable = StringVar(master)

        Label(master, text=text).place(x=x, y=y)

        if disabled:
            self.text_box = Entry(master, textvariable=self.variable, width = width, state = "readonly")
            self.text_box.place(x=x + distance, y=y)
        else:
            self.text_box = Entry(master, textvariable=self.variable, width=width)
            self.text_box.place(x=x + distance, y=y)
