from tkinter import *

root = Tk()

def btnClicked1(event):
    Label(root, text="btnClicked-1").pack()


def btnClicked2(event):
    Label(root, text="btnClicked-2").pack()



myBtn = Button(root, text="Click Here")
# myBtn.bind("<Button-3>", btnClicked)
# myBtn.bind("<Enter>", btnClicked)
# myBtn.bind("<Leave>", btnClicked)
# myBtn.bind("<FocusIn>", btnClicked)
# myBtn.bind("<FocusOut>", btnClicked)
# myBtn.bind("<Return>", btnClicked)     # after focus Enter
# myBtn.bind("<Key>", btnClicked1)          # event.char   #event.keysym
myBtn.bind("<Return>", btnClicked1)
myBtn.bind("<Button-1>", btnClicked2)
myBtn.pack()





root.mainloop()