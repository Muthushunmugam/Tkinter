from tkinter import *

a = Tk()
a.title("GPA")

Label(a, text="GPA CALCULATOR").grid(row=0, column=0)
Label(a, text=" ").grid(row=1, column=0)
Label(a, text="GRADE AND THEIR POINTS - [O:10, A+:9, A:8 , B+:7, B:6, C:5, F:0]").grid(row=2, column=0)
Label(a, text=" ").grid(row=3, column=0)

name1 = Label(a, text="Enter First subject").grid(row=4, column=0)
first = StringVar()
e1 = Entry(a, textvariable=first)
e1.grid(row=4, column=1)

name2 = Label(a, text="Enter Second subject").grid(row=5, column=0)
second = StringVar()
e2 = Entry(a, textvariable=second)
e2.grid(row=5, column=1)

name3 = Label(a, text="Enter Third subject").grid(row=6, column=0)
third = StringVar()
e3 = Entry(a, textvariable=third)
e3.grid(row=6, column=1)

name4 = Label(a, text="Enter Fourth subject").grid(row=7, column=0)
four = StringVar()
e4 = Entry(a, textvariable=four)
e4.grid(row=7, column=1)

name5 = Label(a, text="Enter Fifth subject").grid(row=8, column=0)
five = StringVar()
e5 = Entry(a, textvariable=five)
e5.grid(row=8, column=1)

name6 = Label(a, text="Enter Sixth subject").grid(row=9, column=0)
six = StringVar()
e6 = Entry(a, textvariable=six)
e6.grid(row=9, column=1)

cr1 = Label(a, text="Credits for First subject").grid(row=4, column=2)
credit1 = IntVar()
e7 = Entry(a, textvariable=credit1)
e7.grid(row=4, column=3)

cr2 = Label(a, text="Credits for Second subject").grid(row=5, column=2)
credit2 = IntVar()
e8 = Entry(a, textvariable=credit2)
e8.grid(row=5, column=3)

cr3 = Label(a, text="Credits for Third subject").grid(row=6, column=2)
credit3 = IntVar()
e9 = Entry(a, textvariable=credit3)
e9.grid(row=6, column=3)

cr4 = Label(a, text="Credits for Fourth subject").grid(row=7, column=2)
credit4 = IntVar()
e10 = Entry(a, textvariable=credit4)
e10.grid(row=7, column=3)

cr5 = Label(a, text="Credits for Fifth subject").grid(row=8, column=2)
credit5 = IntVar()
e11 = Entry(a, textvariable=credit5)
e11.grid(row=8, column=3)

cr6 = Label(a, text="Credits for Sixth subject").grid(row=9, column=2)
credit6 = IntVar()
e12 = Entry(a, textvariable=credit6)
e12.grid(row=9, column=3)

g1 = Label(a, text="Grade for First subject").grid(row=4, column=4)
grade1 = StringVar()
e13 = Entry(a, textvariable=grade1)
e13.grid(row=4, column=5)

g2 = Label(a, text="Grade for Second subject").grid(row=5, column=4)
grade2 = StringVar()
e14 = Entry(a, textvariable=grade2)
e14.grid(row=5, column=5)

g3 = Label(a, text="Grade for Third subject").grid(row=6, column=4)
grade3 = StringVar()
e15 = Entry(a, textvariable=grade3)
e15.grid(row=6, column=5)

g4 = Label(a, text="Grade for Fourth subject").grid(row=7, column=4)
grade4 = StringVar()
e16 = Entry(a, textvariable=grade4)
e16.grid(row=7, column=5)

g5 = Label(a, text="Grade for Fifth subject").grid(row=8, column=4)
grade5 = StringVar()
e17 = Entry(a, textvariable=grade5)
e17.grid(row=8, column=5)

g6 = Label(a, text="Grade for Sixth subject").grid(row=9, column=4)
grade6 = StringVar()
e18 = Entry(a, textvariable=grade6)
e18.grid(row=9, column=5)


def gpa():
    x1 = int(e7.get())
    x2 = int(e8.get())
    x3 = int(e9.get())
    x4 = int(e10.get())
    x5 = int(e11.get())
    x6 = int(e12.get())

    y1 = e13.get()
    y2 = e14.get()
    y3 = e15.get()
    y4 = e16.get()
    y5 = e17.get()
    y6 = e18.get()

    n1 = e1.get()
    n2 = e2.get()
    n3 = e3.get()
    n4 = e4.get()
    n5 = e5.get()
    n6 = e6.get()

    if ((y1 == "O") or (y1 == "o")):
        a = x1 * 1
    elif ((y1 == "A+") or (y1 == "a+")):
        a = x1 * 0.9
    elif ((y1 == "A") or (y1 == "a")):
        a = x1 * 0.8
    elif ((y1 == "B+") or (y1 == "b+")):
        a = x1 * 0.7
    elif ((y1 == "B") or (y1 == "b")):
        a = x1 * 0.6
    elif ((y1 == "C") or (y1 == "c")):
        a = x1 * 0.5
    elif ((y1 == "F") or (y1 == "f")):
        a = x1 * 0

    if ((y2 == "O") or (y2 == "o")):
        b = x2 * 1
    elif ((y2 == "A+") or (y2 == "a+")):
        b = x2 * 0.9
    elif ((y2 == "A") or (y2 == "a")):
        b = x2 * 0.8
    elif ((y2 == "B+") or (y2 == "b+")):
        b = x2 * 0.7
    elif ((y2 == "B") or (y2 == "b")):
        b = x2 * 0.6
    elif ((y2 == "C") or (y2 == "c")):
        b = x2 * 0.5
    elif ((y2 == "F") or (y2 == "f")):
        b = x2 * 0

    if ((y3 == "O") or (y3 == "o")):
        c = x3 * 1
    elif ((y3 == "A+") or (y3 == "a+")):
        c = x3 * 0.9
    elif ((y3 == "A") or (y3 == "a")):
        c = x3 * 0.8
    elif ((y3 == "B+") or (y3 == "b+")):
        c = x3 * 0.7
    elif ((y3 == "B") or (y3 == "b")):
        c = x3 * 0.6
    elif ((y3 == "C") or (y3 == "c")):
        c = x3 * 0.5
    elif ((y3 == "F") or (y3 == "f")):
        c = x3 * 0

    if ((y4 == "O") or (y4 == "o")):
        d = x4 * 1
    elif ((y4 == "A+") or (y4 == "a+")):
        d = x4 * 0.9
    elif ((y4 == "A") or (y4 == "a")):
        d = x4 * 0.8
    elif ((y4 == "B+") or (y4 == "b+")):
        d = x4 * 0.7
    elif ((y4 == "B") or (y4 == "b")):
        d = x4 * 0.6
    elif ((y4 == "C") or (y4 == "c")):
        d = x4 * 0.5
    elif ((y4 == "F") or (y4 == "f")):
        d = x4 * 0

    if ((y5 == "O") or (y5 == "o")):
        e = x5 * 1
    elif ((y5 == "A+") or (y5 == "a+")):
        e = x5 * 0.9
    elif ((y5 == "A") or (y5 == "a")):
        e = x5 * 0.8
    elif ((y5 == "B+") or (y5 == "b+")):
        e = x5 * 0.7
    elif ((y5 == "B") or (y5 == "b")):
        e = x5 * 0.6
    elif ((y5 == "C") or (y5 == "c")):
        e = x5 * 0.5
    elif ((y5 == "F") or (y5 == "f")):
        e = x5 * 0

    if ((y6 == "O") or (y6 == "o")):
        f = x6 * 1
    elif ((y6 == "A+") or (y6 == "a+")):
        f = x6 * 0.9
    elif ((y6 == "A") or (y6 == "a")):
        f = x6 * 0.8
    elif ((y6 == "B+") or (y6 == "b+")):
        f = x6 * 0.7
    elif ((y6 == "B") or (y6 == "b")):
        f = x6 * 0.6
    elif ((y6 == "C") or (y6 == "c")):
        f = x6 * 0.5
    elif ((y6 == "F") or (y6 == "f")):
        f = x6 * 0

    mark = a + b + c + d + e + f
    mean = x1 + x2 + x3 + x4 + x5 + x6
    gpa = (mark / mean) * 10

    if ((y1 == "F") or (y1 == "f") or (y2 == "F") or (y2 == "f") or (y3 == "f") or (y3 == "F") or (y4 == "F") or (
            y4 == "f") or (y5 == "F") or (y5 == "f") or (y6 == "F") or (y6 == "F")):
        exit
    else:
        txt = Text(height=1, width=10)
        txt.grid(row=11, column=3)
        txt.insert(END, "GPA = {}".format(gpa))

    print("Subject - gpa")
    print(" ")
    print(n1, "-", a)
    print(n2, "-", b)
    print(n3, "-", c)
    print(n4, "-", d)
    print(n5, "-", e)
    print(n6, "-", f)
    print(" ")

    if ((y1 == "F") or (y1 == "f") or (y2 == "F") or (y2 == "f") or (y3 == "f") or (y3 == "F") or (y4 == "F") or (
            y4 == "f") or (y5 == "F") or (y5 == "f") or (y6 == "F") or (y6 == "F")):
        print("REAPPEAR")
    else:
        print("Total =", gpa)


button = Button(a, text="Calculate", fg='Blue', command=gpa).grid(row=10, column=6)

a.mainloop()