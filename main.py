from tkinter import *
from DateTime import *
from Db import Db
from calculator import open_cal
from models.Finance import Finance
from models.components.Table import Table
from show_add_window import show_add_window

root = Tk()
root.title("Personal Finance Manager")
root.geometry("1100x600")
# root.configure(bg="cyan")

db = Db()

table_paned = PanedWindow()
table_paned.pack(expand=1, fill=BOTH, side=TOP)
Table(table_paned, db.finances)

buttons_paned = PanedWindow()
buttons_paned.pack(fill=BOTH, side=BOTTOM)
button_new = Button(buttons_paned,text="Add",command=lambda :show_add_window(db))
button_new.pack(side=LEFT)

root.mainloop()