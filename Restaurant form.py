from tkinter import *
a=Tk()
a.title("RESTAURANT")
a.configure(bg = 'azure')

Label(a,text="MC DONALDS RESTAURANT",bg = 'azure',font='bold').grid(row=0,column=1)
Label(a,text="",bg = 'azure').grid(row=1,column=0)
Label(a,text="DESERTS",bg = 'azure').grid(row=2,column=0)


a1 = Label(a,text="McFlurry Oreo - rs.90",bg = 'azure')
a2 = Label(a,text="McFlurry Choco crunch - rs.90",bg = 'azure')
a3 = Label(a,text="Soft serve strawberry - rs.70",bg = 'azure')

a1.grid(row=3,column=1)
a2.grid(row=4,column=1)
a3.grid(row=5,column=1)


Label(a,text="FRIES",bg = 'azure').grid(row=2,column=2)
fries = IntVar()

c1 = Label(a,text="Veg Nudgets - rs.50",bg = 'azure')
c2 = Label(a,text="Smileys - rs.30",bg = 'azure')

c1.grid(row=3,column=3)
c2.grid(row=4,column=3)

Label(a,text="SPICY MEALS LARGE",bg = 'azure').grid(row=6,column=0)


b1 = Label(a,text="Chicken Mc spicy - rs.289",bg = 'azure')
b2 = Label(a,text="Paneer Mc spicy - rs.260",bg = 'azure')

b1.grid(row=7,column=1)
b2.grid(row=8,column=1)

Label(a,text="SPICY MEALS ORDINARY",bg = 'azure').grid(row=6,column=2)

b3 = Label(a,text="Mc Aloo Tikki - rs.148",bg = 'azure')
b4 = Label(a,text="Chicken kebab burger - rs.170",bg = 'azure')

b3.grid(row=7,column=3)
b4.grid(row=8,column=3)

Label(a,text=" ",bg = 'azure').grid(row=9,column=0)
Label(a,text="NO. OF ITEMS :",bg = 'azure').grid(row=10,column=0)
Label(a,text=" ",bg = 'azure').grid(row=11,column=0)

Label(a,text="McFlurry Oreo",bg = 'azure').grid(row=12,column=0)
value1 = IntVar()
e1=Entry(a,textvariable = value1)
e1.grid(row=13,column = 0)

Label(a,text="McFlurry Choco crunch",bg = 'azure').grid(row=12,column=1)
value2 = IntVar()
e2=Entry(a,textvariable = value2)
e2.grid(row=13,column = 1)

Label(a,text="Soft serve strawberry",bg = 'azure').grid(row=12,column=2)
value3 = IntVar()
e3=Entry(a,textvariable = value3)
e3.grid(row=13,column = 2)

Label(a,text="Veg Nudgets",bg = 'azure').grid(row=14,column=0)
value4 = IntVar()
e4=Entry(a,textvariable = value4)
e4.grid(row=15,column = 0)

Label(a,text="Smileys",bg = 'azure').grid(row=14,column=1)
value5 = IntVar()
e5=Entry(a,textvariable = value5)
e5.grid(row=15,column = 1)

Label(a,text="Chicken Mc spicy",bg = 'azure').grid(row=16,column=0)
value6 = IntVar()
e6=Entry(a,textvariable = value6)
e6.grid(row=17,column = 0)

Label(a,text="Paneer Mc spicy",bg = 'azure').grid(row=16,column=1)
value7 = IntVar()
e7=Entry(a,textvariable = value7)
e7.grid(row=17,column = 1)

Label(a,text="Mc Aloo Tikki",bg = 'azure').grid(row=16,column=2)
value8 = IntVar()
e8=Entry(a,textvariable = value8)
e8.grid(row=17,column = 2)

Label(a,text="Chicken kebab burger",bg = 'azure').grid(row=16,column=3)
value9 = IntVar()
e9=Entry(a,textvariable = value9)
e9.grid(row=17,column = 3)



def billing():

    x1=e1.get()
    x2=e2.get()
    x3=e3.get()
    x4=e4.get()
    x5=e5.get()
    x6=e6.get()
    x7=e7.get()
    x8=e8.get()
    x9=e9.get()

    total = ((int(x1)*90)+(int(x2)*90)+(int(x3)*70)+(int(x4)*50)+(int(x5)*30)+(int(x6)*289)+(int(x7)*260)+(int(x8)*148)+(int(x9)*170))

    la = Label(a,text = total,font = "Helvetica",bg = 'cyan2').grid(row=19,column=1)
    la2 = Label(a,text = "TOTAL",font = "Helvetica",bg = 'azure').grid(row=19,column=0)

button = Button(a,text="BILL",font = "Helvetica",fg = 'Blue',command = billing).grid(row=18,column=4)


a.mainloop()