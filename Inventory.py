from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database

db = database('store.db')


def populate_list():
    sales_list.delete(0, END)
    for row in db.fetch():
        sales_list.insert(END, row)


def add_product():
    if item_text.get() == '' or customer_text.get() == '' or ID_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required fields', 'Please include all the fields')
        return
    db.insert(item_text.get(), customer_text.get(), ID_text.get(), price_text.get())
    sales_list.delete(0, END)
    sales_list.insert(END,item_text.get(), customer_text.get(), ID_text.get())
    clear_input()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = sales_list.curselection()[0]
        selected_item = sales_list.get(index)

        item_entry.delete(0, END)
        item_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        ID_entry.delete(0, END)
        ID_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])

    except IndexError:
        pass


def remove_product():
    db.remove(selected_item[0])
    clear_input()
    populate_list()


def update_product():
    db.update(selected_item[0], item_text.get(), customer_text.get(), ID_text.get(), price_text.get())
    populate_list()


def clear_input():
    item_entry.delete(0, END)
    customer_entry.delete(0, END)
    ID_entry.delete(0, END)
    price_entry.delete(0, END)


app = Tk()

app.title('Sales Manager')
app.minsize(700, 300)

item_text = StringVar()
item_label = Label(app, text='Product Name: ', font=('bold', 10), pady=20)
item_label.grid(row=0, column=0, sticky=W)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_label = Label(app, text='Customer: ', font=('bold', 10))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

ID_text = StringVar()
ID_label = Label(app, text='Product ID: ', font=('bold', 10))
ID_label.grid(row=1, column=0, sticky=W)
ID_entry = Entry(app, textvariable=ID_text)
ID_entry.grid(row=1, column=1)

price_text = StringVar()
price_label = Label(app, text='Price: ', font=('bold', 10))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)




sales_list = Listbox(app, height=10, width=70, border=0)
sales_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# scrollbar

scrollbar = Scrollbar(app, )
scrollbar.grid(row=3, column=3)

# set scroll to saleslist

sales_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=sales_list.yview)
# bind list
sales_list.bind('<<ListboxSelect>>', select_item)


# Buttons
add_btn = Button(app, text='Add Product', width=12, command=add_product)
add_btn.grid(row=2, column=0, pady=20)


remove_btn = Button(app, text='Remove Product', width=12, command=remove_product)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Product', width=12, command=update_product)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_input)
clear_btn.grid(row=2, column=3)

# populate data
populate_list()


app.mainloop()

