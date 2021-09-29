from tkinter import *

expression = " "

def click(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalclick():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "
    except:
        equation.set("error")
        expression = " "

def clear():
    global expression
    expression = " "
    equation.set(" ")

if __name__ == '__main__':

    a=Tk()
    a.title("CALCULATOR")
    a.configure(bg="azure")

    equation = StringVar()
    e=Entry(a,textvariable=equation,width=30,borderwidth=6).grid(row=0,column=2)

    equation.set("Enter Your Expresssion")
    space = Label(a,text=" ",bg="azure").grid(row=1,column=0)

    b1 = Button(a,text="1",width = 12,command = lambda:click(1)).grid(row=2,column =1)
    b2 = Button(a,text="2",width = 12,command = lambda:click(2)).grid(row=2,column =2)
    b3 = Button(a,text="3",width = 12,command = lambda:click(3)).grid(row=2,column =3)
    b4 = Button(a,text="4",width = 12,command = lambda:click(4)).grid(row=3,column =1)
    b5 = Button(a,text="5",width = 12,command = lambda:click(5)).grid(row=3,column =2)
    b6 = Button(a,text="6",width = 12,command = lambda:click(6)).grid(row=3,column =3)
    b7 = Button(a,text="7",width = 12,command = lambda:click(7)).grid(row=4,column =1)
    b8 = Button(a,text="8",width = 12,command = lambda:click(8)).grid(row=4,column =2)
    b9 = Button(a,text="9",width = 12,command = lambda:click(9)).grid(row=4,column =3)
    b0 = Button(a,text="0",width = 12,command = lambda:click(0)).grid(row=5,column =2)

    b10 = Button(a,text="+",width = 12,command = lambda:click("+")).grid(row=6,column =1)
    b11 = Button(a,text="-",width = 12,command = lambda:click("-")).grid(row=6,column =2)
    b12 = Button(a,text="*",width = 12,command = lambda:click("*")).grid(row=6,column =3)
    b13 = Button(a,text="/",width = 12,command = lambda:click("/")).grid(row=7,column =1)
    b14 = Button(a,text="=",width = 12,command = equalclick).grid(row=7,column =2)
    b15 = Button(a,text=".",width = 12,command = lambda:click(".")).grid(row=7,column =1)
    b16 = Button(a,text="CLEAR",width = 12,command = clear).grid(row=7,column =3)
    a.mainloop()