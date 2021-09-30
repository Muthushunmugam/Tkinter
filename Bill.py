from tkinter import *

a = Tk()

Label(a, text="FRUITS SHOP").grid(row=0, column=1)

Label(a, text="PRICE:").grid(row=1, column=0)

Label(a, text="Apple - rs.35").grid(row=2, column=1)
Label(a, text="Orange - rs.20").grid(row=3, column=1)
Label(a, text="Pome - rs.50").grid(row=4, column=1)
Label(a, text="Lemon - rs.5").grid(row=5, column=1)

Label(a, text="STOCK AVAILABLE:").grid(row=6, column=0)

Label(a, text="Apple - 100").grid(row=7, column=1)
Label(a, text="Orange - 200").grid(row=8, column=1)
Label(a, text="Pome - 60").grid(row=9, column=1)
Label(a, text="Lemon - 200").grid(row=10, column=1)

Label(a, text="Add to your cart: ").grid(row=11, column=0)

apple = Label(a, text="No of apples : ").grid(row=12, column=0)
appl = IntVar()
e1 = Entry(a, textvariable=appl)
e1.grid(row=12, column=1)

orange = Label(a, text="No of oranges : ").grid(row=13, column=0)
orang = IntVar()
e2 = Entry(a, textvariable=orang)
e2.grid(row=13, column=1)

pome = Label(a, text="No of apples : ").grid(row=14, column=0)
pom = IntVar()
e3 = Entry(a, textvariable=pom)
e3.grid(row=14, column=1)

lemon = Label(a, text="No of oranges : ").grid(row=15, column=0)
lem = IntVar()
e4 = Entry(a, textvariable=lem)
e4.grid(row=15, column=1)


def bill():
    x1 = int(e1.get())
    x2 = int(e2.get())
    x3 = int(e3.get())
    x4 = int(e4.get())

    y1 = x1 * 35
    y2 = x2 * 20
    y3 = x3 * 50
    y4 = x4 * 5

    y = y1 + y2 + y3 + y4

    if ((x1 > 100) or (x2 > 200) or (x3 > 60) or (x4 > 200)):
        print("Out of stock")
    else:
        print("YOUR BILL :")
        print(" ")
        print("*APPLE - rs.", y1)
        print("*Orange - rs.", y2)
        print("*Pome - rs.", y3)
        print("*Lemon - rs.", y4)
        print("_____")
        print(" ")
        print("TOTAL - rs.", y)
        print("_____")
        print(" ")
        print("STOCK available : ")
        print(" ")
        print("APPLE = ", 100 - x1)
        print("Orange = ", 200 - x2)
        print("Pome = ", 60 - x3)
        print("Lemon = ", 200 - x4)


b = Button(a, text="Bill", fg="Blue", command=bill)
b.grid(row=16, column=3)

a.mainloop()