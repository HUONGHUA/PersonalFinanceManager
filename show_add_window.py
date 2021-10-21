
from tkinter import *
from calculator import open_cal

from models.Finance import Finance

def show_add_window(db):
    top = Toplevel()
    top.title('Add new finance infomation')
    top.geometry('500x500')

    datetime_label = Label(master=top, bg="black", fg='white', text='1) Enter Time(dd/mm/yyyy): ')
    datetime_label.place(x=30, y=30)
    datetime_input = Entry(top,width=20,font=("Helvetica", 16))
    datetime_input.place(x=250, y=30)

    #Label and Button Object

    category_label = Label(master=top, bg="black", fg='white', text='2) Choose your Object: ')
    category_label.place(x=30, y=70)
    category_click = StringVar()
    category_click.set('Vui long chọn!')
    category_select = OptionMenu(top, category_click, 'Cafe', 'Breakfast', 'Dinner', 'Market', 'Other')
    category_select.place(x=250, y=70)

    #Label and Entry Money , Open Calculation
    money_label = Label(master=top, bg="black", fg='white', text='3) Enter your Money: ')
    money_label.place(x=30, y=110)

    money_input = Entry(top,width=20,font=("Helvetica", 16))
    money_input.place(x=250, y=110)

    cal_label = Button(top, text='Open Calculation',command=open_cal).pack()

    #Label and button Type
    type_label = Label(master=top, bg="black", fg='white', text='4) Choose type : ')
    type_label.place(x=30, y=150)

    type_click = StringVar()
    type_click.set('Vui long chọn!')

    type_select = OptionMenu(top, type_click, 'Buy', 'Pay')
    type_select.place(x=250, y=150)


    #Label and Entry Note
    note_label = Label(master=top, bg="black", fg='white', text='5) Enter Note : ')
    note_label.place(x=30, y=190)
    note_input = Entry(top,width=20,font=("Helvetica", 16))
    note_input.place(x=250, y=190)

    #Save data

    def save_handler():
        finance = Finance(
            datetime=datetime_input.get(),
            category=category_click.get(),
            money=money_input.get(),
            type=type_click.get(),
            note=note_input.get()
        )
        db.addFinance(finance)
    save_button = Button(top, text="Click to Save !", font=("Helvetica", 30), fg="red", command=save_handler)
    save_button.place(x=100, y=280)
    mainloop()
