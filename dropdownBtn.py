from tkinter import *

root = Tk()
root.title("Drop Down Menu");
root.geometry("400x500")

def submitDD():
    Label(root, text=a.get()).pack()


a = StringVar()
a.set("Select Language")

ddBtn = OptionMenu(root, a, "Python", "PHP", "Node", "React").pack()

Button(root, text="Submit", command=submitDD).pack()




root.mainloop()