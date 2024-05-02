from tkinter import StringVar, Label,Entry


class TextWithLabel:
    def __init__(self, master, text,x,y,distance=60, disabled = False):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.distance = distance
        self.variable = StringVar()

        Label(master, text=text).place(x=x, y=y)

        if disabled:
            self.text_box = Entry(master, textvariable=self.variable,state="readonly")
            self.text_box.place(x=x + distance, y=y)
        else:
            self.text_box = Entry(master, textvariable=self.variable)
            self.text_box.place(x=x + distance, y=y)