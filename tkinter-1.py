from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Creating a label
myLabel1 = Label(text="Hello, Learner 1", anchor="s", bg="red",
                 padx=20,
                 cursor="arrow", fg="white", justify="left")
myLabel2 = Label(text="Hello, Learner 2")
myLabel3 = Label(text="Hello, Learner 3")

# showing it onto screen
myLabel1.pack()
# myLabel2.pack()
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
# myLabel3.grid(row=2, column=3)

root.geometry("560x830")

# img = PhotoImage(file="back2.png")
# photo = Label(root, image=img)
# photo.pack()


def myFunc():
    Label(text="hello Learner").pack()

root.minsize(300, 300)
root.maxsize(1200, 1200)

myBtn = Button(text="Click Here", command=myFunc)
myBtn.pack()


canvas = Canvas(root, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("back2.png"))
canvas.create_image(20, 20, anchor=NW, image=img)



root.mainloop()