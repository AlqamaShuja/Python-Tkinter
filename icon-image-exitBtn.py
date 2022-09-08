from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image-Icon-Exit_Button")
icon = PhotoImage(file="icon-1.png")
# root.iconbitmap("icon-1.png")
# root.iconphoto(False, icon)

img1 = ImageTk.PhotoImage(Image.open("back1.jpg"))
imgLabel = Label(root, image=img1, width=30, height=30)
imgLabel.pack()

root.iconphoto(False, img1)

button_quit = Button(root, text="Quit Program", command=root.quit)
button_quit.pack()


root.mainloop()