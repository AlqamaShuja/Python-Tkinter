from tkinter import *

root = Tk()
root.title("Tkinter Class 2")

root.geometry("500x500")

f1 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

label1 = Label(f1, text="Label 1 Here")
label1.pack(pady=5)
label2 = Label(f1, text="Label 2 Here")
label2.pack(pady=5)

# Frame 2
f2 = Frame(root, borderwidth=8, bg="green", relief=SUNKEN)
f2.pack(fill=X)

label3 = Label(f2, text="Label 3 Here")
label3.grid(row=0, column=0)
label4 = Label(f2, text="Label 4 Here")
label4.grid(row=0, column=1)

x = 3

def submit():
    msg = "Hello, " + name.get()
    Label(f2, text=msg).grid(row=x, column=1)


name = Entry(f2, width=60)
name.grid(row=1, column=0, columnspan=2)
# name.insert(0, "Enter your name")

sub1 = Button(f2, text="Submit", command=submit)
sub1.grid(row=2, column=1)


root.mainloop()