from tkinter import *

class Table:
    def __init__(self,root,finances):
        for i in range(len(finances)):
            self.e = Entry(root)
            self.e.grid(row=i, column=0)
            self.e.insert(END, finances[i].datetime)

            self.e = Entry(root, width=20)
            self.e.grid(row=i, column=1)
            self.e.insert(END, finances[i].category)

            self.e = Entry(root)
            self.e.grid(row=i, column=2)
            self.e.insert(END, finances[i].money)

            self.e = Entry(root)
            self.e.grid(row=i, column=3)
            self.e.insert(END, finances[i].type)

            self.e = Entry(root)
            self.e.grid(row=i, column=4)
            self.e.insert(END, finances[i].note)

            self.e = Button(root, text='Update')
            self.e.grid(row=i, column=5)
