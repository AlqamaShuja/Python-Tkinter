from tkinter import *
root = Tk()

def radioBtnClicked():
    label1 = Label(root, text=a.get())
    label1.pack()


a = IntVar()
a.set(1)

Radiobutton(root, text="Opt 1", variable=a, value=1, command=radioBtnClicked).pack()
Radiobutton(root, text="Opt 2", variable=a, value=2, command=radioBtnClicked).pack()
Radiobutton(root, text="Opt 3", variable=a, value=3, command=radioBtnClicked).pack()

label1 = Label(root, text=a.get())
label1.pack()


root.mainloop()