from tkinter import *
import datetime

a = Tk()
a.title("AGE CALCULATOR")
a.geometry("400x150")

title = Label(a, text="ENTER YOUR BIRTH DATE,MONTH AND YEAR").grid(row=0, column=1)
date = Label(a, text="DAY :").grid(row=1, column=0)
d1 = Entry(a)
d1.grid(row=1, column=1)

month = Label(a, text="MONTH :").grid(row=2, column=0)
m1 = Entry(a)
m1.grid(row=2, column=1)

year = Label(a, text="YEAR :").grid(row=3, column=0)
y1 = Entry(a)
y1.grid(row=3, column=1)


def calculate():
    d = int(d1.get())
    m = int(m1.get())
    y = int(y1.get())

    bornday = datetime.date(y, m, d)
    today = datetime.date.today()
    age = today.year - bornday.year

    txt = Text(height=3, width=20)
    txt.grid(row=6, column=1)
    txt.insert(END, "You are {} years old".format(age))


Button1 = Button(a, text="CALCULATE", fg="Blue", command=calculate)
Button1.grid(row=4, column=2)

a.mainloop()