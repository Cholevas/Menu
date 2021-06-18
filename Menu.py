from tkinter import *
from tkinter import messagebox

root = Tk()
xy = 0

lbl = Label(root, text="Salads")
lbl.grid(column=0, row=0)
var = IntVar()
r1 = Radiobutton(root, text="Greek Salad", variable=var, value=0)
r1.grid(column=0, row=1)
r2 = Radiobutton(root, text="Fruit Salad", variable=var, value=1)
r2.grid(column=0, row=2)
r3 = Radiobutton(root, text="Caesar Salad", variable=var, value=2)
r3.grid(column=0, row=3)

lbl = Label(root, text="Dinner")
lbl.grid(column=1, row=0)
rad = IntVar()
r4 = Radiobutton(root, text="Tofu Stir-Fry", variable=rad, value=0)
r4.grid(column=1, row=1)
r5 = Radiobutton(root, text="Salsa Verde Enchiladas", variable=rad, value=1)
r5.grid(column=1, row=2)
r6 = Radiobutton(root, text="Shrimps", variable=rad, value=2)
r6.grid(column=1, row=3)

lbl = Label(root, text="Refreshments")
lbl.grid(column=2, row=0)
cap = IntVar()
r7 = Radiobutton(root, text="Coca-Cola", variable=cap, value=0)
r7.grid(column=2, row=1)
r8 = Radiobutton(root, text="Pepsi", variable=cap, value=1)
r8.grid(column=2, row=2)
r9 = Radiobutton(root, text="Beer", variable=cap, value=2)
r9.grid(column=2, row=3)


def ready():
    global xy
    x=var.get()
    y=rad.get()
    z=cap.get()
    if x == 0:
        xy = xy + 12
    elif x == 1:
        xy = xy + 10
    elif x == 2:
        xy = xy + 11

    if y == 0:
        xy = xy + 25
    elif y == 1:
        xy = xy + 29
    elif y == 2:
        xy = xy + 32

    if z == 0:
        xy = xy + 1
    elif z == 1:
        xy = xy + 1
    elif z == 2:
        xy = xy + 3

    messagebox.showinfo("Check",str(xy)+"$")
    xy=0

btn = Button(root, text="Ready", command=ready)
btn.grid(column=3, rowspan=4, row=1)

root.mainloop()
