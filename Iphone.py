from tkinter import *

a = Tk()

a.title("Iphone sale")

i1 = Label(a, text="1.Apple iphone 7 (32GB)-Black", font="Bold")
i2 = Label(a, text="Price : rs.24,990 & Rating : 4.5/5")
i3 = Label(a, text=" ")
i1.grid(row=1, column=1)
i2.grid(row=2, column=1)
i3.grid(row=3, column=1)

i4 = Label(a, text="2.Apple iphone 11 (64GB)-Blue", font="Bold")
i5 = Label(a, text="Price : rs.49,990 & Rating : 4.0/5")
i6 = Label(a, text=" ")
i4.grid(row=5, column=1)
i5.grid(row=6, column=1)
i6.grid(row=7, column=1)

i7 = Label(a, text="3.Apple iphone 11 Pro max (512GB)-Gray", font="Bold")
i8 = Label(a, text="Price : rs.1,50,000 & Rating : 4.7/5")
i9 = Label(a, text=" ")
i7.grid(row=9, column=1)
i8.grid(row=10, column=1)
i9.grid(row=11, column=1)

i10 = Label(a, text="9.Apple iphone 12 (128GB)-White", font="Bold")
i11 = Label(a, text="Price : rs.79,990 & Rating : 5/5")
i12 = Label(a, text=" ")
i10.grid(row=13, column=1)
i11.grid(row=14, column=1)
i12.grid(row=15, column=1)

i13 = Label(a, text="Sort by :")
i13.grid(row=16, column=0)

radio = IntVar()
r1 = Radiobutton(a, text="What's New", variable=radio, value=1)
r1.grid(row=17, column=1)
r2 = Radiobutton(a, text="High to Low", variable=radio, value=2)
r2.grid(row=18, column=1)
r3 = Radiobutton(a, text="Low to High", variable=radio, value=3)
r3.grid(row=19, column=1)
r4 = Radiobutton(a, text="Customer rating", variable=radio, value=4)
r4.grid(row=20, column=1)


def sortby():
    print("Sorted List")

    print(" ")

    global sort
    sort = radio.get()
    a.quit()

    if (sort == 1):
        print("Iphone-12 -> Iphone-11 pro -> Iphone-11 -> Iphone-7")
    if (sort == 2):
        print("Iphone-11 pro -> Iphone-12 -> Iphone-11 -> Iphone-7")
    if (sort == 3):
        print("Iphone-7 -> Iphone-11 -> Iphone-12 -> Iphone-11 pro")
    if (sort == 4):
        print("Iphone-12 -> Iphone-11 pro -> Iphone-7 ->Iphone-11")


s = Button(a, text="Sort", command=sortby)
s.grid(row=21, column=2)

a.mainloop()