from tkinter import *
from PIL import ImageTk, Image

root = Tk()

icon = ImageTk.PhotoImage(Image.open("icon-1.png"))
# icon_label = Label(root, image=icon);
root.iconphoto(False, icon)

def openNewWindow():
    top = Toplevel()
    lb1_top = Label(top, text="Hello").pack()
    top.title("Kala kala")
    global icon_top
    icon_top = ImageTk.PhotoImage(Image.open("images/icon-2.png"))
    top.iconphoto(False, icon_top)
    Label(top, image=icon_top).pack()
    Button(top, text="Close Window", command=top.destroy).pack()


Button(root, text="Open Window", command=openNewWindow).pack()

root.mainloop()