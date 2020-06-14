from tkinter import *
from datetime import datetime
import fileinput

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
dt = Label(root, text="Title: ")
dt.grid(row=1, column=4)

b = Entry(root, width=20)
b.grid(row=2, column=5)
bt = Label(root, text="Context: ")
bt.grid(row=2, column=4)

de = Entry(root, width=20)
de.grid(row=3, column=5)
det = Label(root, text="Delete: ")
det.grid(row=3, column=4)


# Function of counting lines
file = open("/Users/mac/Desktop/plan.txt", "r")
number_of_lines = 0
for line1 in file:
    line1 = line1.strip("\n")
    number_of_lines += 1


# Function of Save
def myclick():
    global number_of_lines
    Title = d.get()
    Content = b.get()
    with open("/Users/mac/Desktop/plan.txt", 'a+') as f:
        f.write("\n")
        f.write(str(datetime.date(datetime.now())))
        f.write("-'" + str(number_of_lines) + "'")
        f.write("- Title: ")
        f.write(Title)
        f.write(" - Content: ")
        f.write(Content)
        f.write("\n")
    h = Label(root, text="Saved well")
    h.grid(row=9, column=5)
    number_of_lines += 1


# Function of Search
def rice():
    n = 0
    with open("/Users/mac/Desktop/plan.txt", 'r') as f:
        for line in f.readlines():
            if not line.find(e.get()):
                texts = Label(root, text=line)
                texts.grid(row=n, column=0)
                n += 1
    h = Label(root, text="Searched well")
    h.grid(row=9, column=5)


# Function of delete
def delete():
    with open("/Users/mac/Desktop/plan.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if de.get() not in line:
                f.write(line)
        f.truncate()
    h = Label(root, text="Deleted well")
    h.grid(row=9, column=5)


# Function of clear
def clear():
    for i in range(100):
        texts1 = Label(root, text="\t\t\t\t\t\t\t")
        texts1.grid(row=i, column=0)
        texts2 = Label(root, text="\t\t\t\t\t\t\t")
        texts2.grid(row=i+1, column=0)
        texts3 = Label(root, text='\t\t\t\t\t\t\t')
        texts3.grid(row=i+2, column=0)
    h = Label(root, text="Cleared well")
    h.grid(row=9, column=5)


# Function for removing empty lines
def empty():
    for line in fileinput.FileInput("/Users/mac/Desktop/plan.txt", inplace=1):
        if line.rstrip():
            print(line)
    h = Label(root, text="Removed well")
    h.grid(row=9, column=5)


# Save Button
save_Button = Button(root, text="Save", command=myclick)
save_Button.grid(row=4, column=5)

# Search Button
search_button = Button(root, text="Search", command=rice)
search_button.grid(row=7, column=5)

# Delete Button
delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=5, column=5)

# Clear Button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=6, column=5)

# Empty Button
empty_button = Button(root, text="Empty", command=empty)
empty_button.grid(row=8, column=5)

# End of Tkinter
root.mainloop()
