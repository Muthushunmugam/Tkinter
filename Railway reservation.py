# RAILWAY RESERVATION FORM

from tkinter import *

a = Tk()

a.title("RAILWAY RESERVATION FORM")

Label(a, text="RAILWAY RESRVATION FORM", font="Bold").grid(row=0, column=1)

Label(a, text="  ").grid(row=1, column=0)

Label(a, text="TRAINS AVAILABLE").grid(row=2, column=0)

Label(a, text="[1]  12163 - Chennai Express").grid(row=3, column=1)

Label(a, text="[2]  12780 - Goa Express").grid(row=4, column=1)

Label(a, text="[3]  12603 - Hyderabad Express").grid(row=5, column=1)

Label(a, text="[4]  12637 - Pandian Express").grid(row=6, column=1)

Label(a, text="SELECT THE TRAIN: ").grid(row=7, column=0)

var = IntVar()

t1 = Radiobutton(a, text="Chennai Express", variable=var, value=1)

t2 = Radiobutton(a, text="Goa Express", variable=var, value=2)

t3 = Radiobutton(a, text="Hyderabad Express", variable=var, value=3)

t4 = Radiobutton(a, text="Pandian Express", variable=var, value=4)

t1.grid(row=8, column=1)

t2.grid(row=8, column=2)

t3.grid(row=9, column=1)

t4.grid(row=9, column=2)

Label(a, text=" ").grid(row=10, column=0)

name = Label(a, text="Name").grid(row=11, column=0)

namevalue = StringVar()

e1 = Entry(a, textvariable=namevalue)

e1.grid(row=11, column=1)

age = Label(a, text="Age").grid(row=12, column=0)

agevalue = IntVar()

e2 = Entry(a, textvariable=agevalue)

e2.grid(row=12, column=1)

Label(a, text=" ").grid(row=13, column=0)

Label(a, text="Gender").grid(row=14, column=0)

var1 = IntVar()

m = Radiobutton(a, text="Male", variable=var1, value=1)

f = Radiobutton(a, text="Female", variable=var1, value=2)

m.grid(row=14, column=1)

f.grid(row=14, column=2)

Label(a, text=" ").grid(row=15, column=0)

Label(a, text="Select train time").grid(row=16, column=0)

time = IntVar()

time1 = Radiobutton(a, text="11.00", variable=time, value=1)

time2 = Radiobutton(a, text="23.00", variable=time, value=2)

time1.grid(row=16, column=1)

time2.grid(row=16, column=2)

Label(a, text="").grid(row=17, column=1)

Label(a, text="FIRST CLASS - AC; SECOND CLASS - AC; SECOND CLASS - NON AC").grid(row=18, column=1)

Label(a, text="").grid(row=19, column=0)

typeof = Label(a, text="SELECT COMPARTMENT").grid(row=20, column=0)

typeof = StringVar()

ty = Entry(a, textvariable=typeof)

ty.grid(row=20, column=1)

Label(a, text="").grid(row=21, column=0)

Label(a, text="Select Berth").grid(row=22, column=0)

berth = IntVar()

berth1 = Radiobutton(a, text="Upper berth", variable=berth, value=1)

berth2 = Radiobutton(a, text="Lower berth", variable=berth, value=2)

berth1.grid(row=22, column=1)

berth2.grid(row=22, column=2)


def submit():
    print("HAVE A NICE JOURNEY... RESERVATION CONFIRMED")

    global trainname
    trainname = var.get()
    a.quit()
    if (trainname == 1):
        print(" Train name - [1]  12163 - Chennai Express")
    elif (trainname == 2):
        print(" Train name - [2]  12780 - Goa Express")
    elif (trainname == 3):
        print(" Train name - [3]  12603 - Hyderabad Express")
    elif (trainname == 4):
        print(" Train name - [4]  12637 - Pandian Express")
    print(" ")

    x1 = e1.get()
    x2 = e2.get()
    print("Name : ", x1)
    print(" ")
    print("Age : ", x2)
    print(" ")

    global gender
    gender = var1.get()
    a.quit()
    if (gender == 1):
        print("Gender : Male")
    elif (gender == 2):
        print("Gender : Female")
    print(" ")

    global j
    j = time.get()
    a.quit()
    if (j == 1):
        print("Time of journey = 11.00")
    if (j == 2):
        print("Time of journey = 23.00")
    print(" ")

    x3 = ty.get()
    print("Class - ", x3)
    print(" ")

    global settle
    settle = berth.get()
    a.quit()
    if (settle == 1):
        print("Berth = Upper")
    if (settle == 2):
        print("Berth = Lower")
    print(" ")


sub = Button(a, text="SUBMIT", fg="Blue", command=submit)
sub.grid(row=23, column=2)
a.mainloop()