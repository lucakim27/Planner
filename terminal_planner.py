from datetime import date
import os


def writing():

    today = date.today()

    d = today.strftime("%b-%d-%Y")

    save_path = '/Users/ubc/Development/PythonProjects/PythonProject1/Planner/planner_files'

    completeName = os.path.join(save_path, d + ".txt")

    file1 = open(completeName, "a")
    
    print("\n")
    content = raw_input("Enter the cotent: ")
    print("\n")
    file1.write(content + "\n")

    file1.close()


def viewing():

    arr = os.listdir('./planner_files')
    
    count = 0
    list1 = []

    for i in arr:
        print(count, i)
        list1.append(i)
        count += 1

    number = raw_input("\nEnter a file number: ")
    
    print("\n")

    try:
        file2 = open("/Users/ubc/Development/PythonProjects/PythonProject1/Planner/planner_files/" + list1[int(number)],"r")
        print("--------------------------------------\n")
        print(file2.read())
        print("--------------------------------------\n")
    except:
        print("There's no such file")



def deleting():

    arr = os.listdir('./planner_files')
    
    count = 0
    list1 = []

    for i in arr:
        print(count, i)
        list1.append(i)
        count += 1

    number = raw_input("\nEnter a file number: ")

    print("\n")

    try:
        
        file1 = open("/Users/ubc/Development/PythonProjects/PythonProject1/Planner/planner_files/" + list1[int(number)], "r")
        
        print("------------------------\n")
        count3 = 0
        list3 = []
        for i in file1.readlines():
            print(count3, i[:len(i)-1])
            list3.append(i[:len(i)-1])
            count3 += 1
        print("\n------------------------\n")

        word = raw_input("Enter a line number: ")

        file2 = "/Users/ubc/Development/PythonProjects/PythonProject1/Planner/planner_files/" + list1[int(number)]

        with open(file2, "r") as f:
            lines = f.readlines()
        with open(file2, "w") as f:
            for line in lines:
                try:
                    if line.strip("\n") != list3[int(word)]:
                        f.write(line)
                except:
                    print("There's no such line")

    except:
        print("There's no such file")








"""
Home in which user choose where to go to and by choosing the number, it calls the function.
"""
while(True):
    print("Writing: 1")
    print("Viewing: 2")
    print("Deleting: 3")
    print("Exit: -1")

    num = raw_input("Choose: ")

    if num == "1":
        writing()
    elif num == "2":
        viewing()
    elif num == "3":
        deleting()
    elif num == "-1":
        break
    else:
        print("Error")
