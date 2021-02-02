import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import sqlite3 as sq

root = tk.Tk()
root.title('Planner')
root.geometry("530x300+500+500")

#  Making a database file called "planner.db"
conn = sq.connect('PlannerDB.db')

# The database will be saved in the location where your 'py' file is saved
cur = conn.cursor()

# Create table - PLANNER
cur.execute('''CREATE TABLE IF NOT EXISTS PLANNER
             ([Tasks] text, [Date] date)''')

task = []

# clear tkinter listbox
def clearList():
    t.delete(0,'end')


def addTask():
    word = e1.get()
    date = cal.get_date()
    rows = [(word, date)]
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    elif l1.cget("text")=="":
        messagebox.showinfo('Empty Entry', 'Enter date')
    else:
        task.append(word)
        cur.executemany('INSERT INTO PLANNER VALUES (?, ?)', rows)
        selectDate()
        e1.delete(0,'end')


# If the value you delete exists then it also gets deleted on any dates.
def delOne():
    try:
        val = t.get(t.curselection())
        cur.execute('DELETE FROM PLANNER WHERE Tasks = (?)', (val,))
        selectDate()
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')


def deleteAll():
    mb = messagebox.askyesno('Delete All','Are you sure?')
    date = cal.get_date()
    if mb==True:
        cur.execute('DELETE FROM PLANNER WHERE Date = (?)', (date,))
        selectDate()


def bye():
    root.destroy()


def selectDate():
    l1["text"] = cal.get_date()
    clearList()
    cur.execute("SELECT * FROM PLANNER")
    values = []
    for val in cur:
        if (str(cal.get_date()) == val[1]):
            values.append(val[0])

    for i in values:
        t.insert("end", i)


l1 = ttk.Label(root, text="")
l1.place(x=370 ,y=30)
l2 = ttk.Label(root, text='Enter down below')
e1 = ttk.Entry(root, width=21)
t = tk.Listbox(root, height=11, selectmode='SINGLE')
b1 = ttk.Button(root, text='Add task', width=20, command=addTask)
b2 = ttk.Button(root, text='Delete', width=20, command=delOne)
b3 = ttk.Button(root, text='Delete all', width=20, command=deleteAll)
b4 = ttk.Button(root, text='Exit', width=20, command=bye)
b5 = ttk.Button(root, text='Select', width=20, command=selectDate)
cal = DateEntry(root, width=30, bg="darkblue", fg="black", year=2021)
cal.grid()


#Place geometry
l2.place(x=90, y=50)
e1.place(x=50, y=80)
b1.place(x=40, y=110)
b2.place(x=40, y=140)
b3.place(x=40, y=170)
b4.place(x=40, y =200)
b5.place(x=300, y=0)
t.place(x=320, y=50)
root.mainloop()

conn.commit()
cur.close()
