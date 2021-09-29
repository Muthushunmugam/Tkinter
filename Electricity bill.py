import tkinter as tk

tit = tk.Tk()
tit.configure(bg="White")
tit.geometry("200x200")


def billcalculation():
    try:
        pre = int(e1.get())
        cur = int(e2.get())
        val = cur - pre
        bill = float(0)

        if (val <= 200):
            if (val < 100):
                bill = 0.0
            elif (val > 100):
                c = val - 100
                bill = float(val * 1.5)

        elif (val > 200 and val <= 500):
            bill = float(bill + (100 * 2))
            c = val - 200
            c = float(c * 3)
            bill = bill + c

        elif (val > 500):
            bill = float(bill + ((3.5 * 100) + (4.6 * 300)))
            c = val - 500
            c = float(c * 6.6)
            bill = bill + c
        bill = round(bill, 2)
        answer = (str(bill) + "+ service taxes")
        # print(answer)
        e3.insert(0, answer)

    except ValueError:
        l6 = tk.Label(tit, text="Enter only numbers", font=("Times", 16), fg="Red")
        l6.grid(column=4, row=5)


l1 = tk.Label(tit, text="Electricity bill calculator", font=("Arial Bold", 28))
l1.grid(column=3, row=0)

l2 = tk.Label(tit, text="Enter your last recorded reading: ", font=("Times", 16))
l2.grid(column=0, row=1)

e1 = tk.Entry(tit, bd=5, font=("Times", 16))
e1.grid(column=2, row=1)

l4 = tk.Label(tit, text="Enter your current reading: ", font=("Times", 16))
l4.grid(column=0, row=3)

e2 = tk.Entry(tit, bd=5, font=("Times", 16))
e2.grid(column=2, row=3)

l3 = tk.Label(tit, text="The Bill is: ", font=("Times", 16))
l3.grid(column=2, row=5)

e3 = tk.Entry(tit, bd=5, font=("Times", 16))
e3.grid(column=2, row=5)

bt = tk.Button(tit, text="CALCULATE", padx=7, pady=7, fg="Black", activebackground="Green", font=("Arial Bold", 14),
               command=billcalculation)
bt.grid(column=3, row=7)
tit.mainloop()