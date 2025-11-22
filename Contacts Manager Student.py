from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
win = Tk()

db = Database('d:/ContactsManager1.db')

def show_list():   
    pass
def add_item():
    pass
def select_item(event):    
    pass

def remove_item():
    pass

def update_item():
    pass
def clear_text():
    pass
def search():
    pass
    
def exit():
    pass



print('&&&&&&&&&&&&&&&&&')

name_text = StringVar()
name_label = Label(win, text = "Name:", font = ('Tahoma 14'))
name_label.place(x = 70 , y = 5)
name_entry = Entry(win, textvariable = name_text, bd = 3, relief = GROOVE)
name_entry.place(x = 137 , y = 5)


address_text = StringVar()
address_label = Label(win, text = "Address:", font = ('Tahoma', 14))
address_label.place(x = 275 , y = 5)
address_entry = Entry(win, textvariable = address_text, bd = 3, relief = GROOVE)
address_entry.place(x = 360 , y = 5)


family_text = StringVar()
family_label = Label(win, text = "Family:", font = ('Tahoma', 14))
family_label.place(x = 70 , y = 35)
family_entry = Entry(win, textvariable = family_text, bd = 3, relief = GROOVE)
family_entry.place(x = 137 , y = 35)


phone_text = StringVar()
phone_label = Label(win, text = "Phone:", font = ('Tahoma', 14))
phone_label.place(x = 275 , y = 35)
phone_entry = Entry(win, textvariable = phone_text, bd = 3, relief = GROOVE)
phone_entry.place(x = 360 , y = 35)


contact_list = Listbox(win, height = 9, width = 100 ,bd = 3)    
contact_list.place(x = 0 , y = 160)


contact_list.bind('<<ListboxSelect>>', select_item)


scrollbar = Scrollbar(win)
scrollbar.place(x = 700 , y = 200)


contact_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = contact_list.yview)

# ضخامت برجسته‌سازی فوکوس. مقدار پیش‌فرض 1 است.
#  برای حذف نمایش برجسته‌سازی فوکوس، مقدار highlightthickness=0 را تنظیم کنید.
add_btn = Button(win, text = "اضافه کردن", width = 18, command = add_item,
                 highlightthickness=2)
add_btn.place(x = 500 , y = 20)

remove_btn = Button(win, text = "حذف کردن", width = 18, command = remove_item)
remove_btn.place(x = 500 , y = 55)

update_btn = Button(win, text = "بروزرساني", width = 18, command = update_item)
update_btn.place(x = 650 , y = 20)

clear_btn = Button(win, text = "پاک کردن ورودي ها", width = 18, command = clear_text)
clear_btn.place(x = 650 , y = 55)

show_btn = Button(win, text = "نمایش لیست", width = 18, command = show_list)
show_btn.place(x = 450 , y = 125)

search_btn = Button(win, text = "جستجو", width = 18, command = search )
search_btn.place(x = 120 , y = 100)

search_text = StringVar()
search_entry = Entry(win, textvariable = search_text, bd = 3, relief = GROOVE)
search_entry.place(x = 275 , y = 100)

exit_a = Button(win, text = "خروج", width = 18, command = exit)
exit_a.place(x = 600 , y = 350)

search_label = Label(win)
search_label.grid(row= 3, column= 3)
win.title("مديريت مخاطبين")
win.geometry('800x400')
win.resizable(0, 0)
win.configure(bg = 'cyan')

win.mainloop()
