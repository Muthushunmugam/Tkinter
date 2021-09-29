from tkinter import *

a=Tk()
a.title("Phone Book")
a.configure(bg="azure")

name=Label(a,text="Name :",bg="azure").grid(row=0,column=0)

e1=Entry(a)
e1.grid(row=0,column=1)

number =Label(a,text="Phone No :",bg="azure").grid(row=1,column=0)

e2=Entry(a)
e2.grid(row=1,column=1)


def save():

    x1=e1.get()
    x2=e2.get()

    print("Name ",x1)
    print("Phone No ",x2)

    b=Toplevel()
    b.configure(bg="azure")
    b.title("Save")

    Label(b,text="Do you want to save the contact?",bg="azure").grid(row=0,column=0)

    button0 = Button(b,text = "YES",bg = "Cyan2",command = s).grid(row=1,column=1)

def s():

    c=Toplevel()
    c.configure(bg="azure")

    Label(c,text="Saved...",bg="Cyan2").grid(row = 0,column = 1)

button=Button(a,text="Save",bg="cyan2",command=save).grid(row=2,column=2)
