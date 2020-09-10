from tkinter import *
from datetime import datetime

# Tkinter
root = Tk()
root.title("Plan Saver")

# blanks and texts grids
e = Entry(root, width=20)
e.grid(row=0, column=5)
et = Label(root, text="Search: ")
et.grid(row=0, column=4)

d = Entry(root, width=20)
d.grid(row=1, column=5)
dt = Label(root, text="Content: ")
dt.grid(row=1, column=4)

de = Entry(root, width=20)
de.grid(row=2, column=5)
det = Label(root, text="Delete: ")
det.grid(row=2, column=4)


# Function of counting lines
def counting_the_number_of_lines():
    number_of_lines = 0
    thefile = open("your text file route")
    while 1:
        buffer = thefile.read(65536)
        if not buffer:
            break
        number_of_lines += buffer.count('\n')
    return number_of_lines


# Function of Save
def myclick():
    content = d.get()
    with open("your text file route", 'a+') as f:
        f.write("\n")
        f.write(str(datetime.date(datetime.now())))
        f.write(" '" + str(counting_the_number_of_lines()) + "'")
        f.write(" - ")
        f.write(content)
        f.write("\n")


# Function of Search
def rice():
    n = 0
    with open("your text file route", 'r') as f:
        for line in f.readlines():
            if not line.find(e.get()):
                texts = Label(root, text=line)
                texts.grid(row=n, column=6)
                n += 1
    h = Label(root, text="Searched well")
    h.grid(row=7, column=5)


# Function of delete
def delete():
    with open("your text file route", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if de.get() not in line:
                f.write(line)
        f.truncate()
    h = Label(root, text="Deleted well")
    h.grid(row=7, column=5)


# Function of clear
def clear():
    for i in range(100):
        texts1 = Label(root, text="\t\t\t\t\t\t\t\t")
        texts1.grid(row=i, column=6)
        texts2 = Label(root, text="\t\t\t\t\t\t\t\t")
        texts2.grid(row=i+1, column=6)
        texts3 = Label(root, text="\t\t\t\t\t\t\t\t")
        texts3.grid(row=i+2, column=6)
    h = Label(root, text="Cleared well")
    h.grid(row=7, column=5)


# Save Button
save_Button = Button(root, text="Save", highlightbackground='#3E4149', command=myclick)
save_Button.grid(row=3, column=5)

# Search Button
search_button = Button(root, text="Search", highlightbackground='#3E4149', command=rice)
search_button.grid(row=6, column=5)

# Delete Button
delete_button = Button(root, text="Delete", highlightbackground='#3E4149', command=delete)
delete_button.grid(row=4, column=5)

# Clear Button
clear_button = Button(root, text="Clear", highlightbackground='#3E4149', command=clear)
clear_button.grid(row=5, column=5)

# End of Tkinter
root.mainloop()
