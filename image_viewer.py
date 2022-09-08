from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img1 = ImageTk.PhotoImage(Image.open("./images/image1.png"))
img2 = ImageTk.PhotoImage(Image.open("./images/image2.png"))
img3 = ImageTk.PhotoImage(Image.open("./images/image3.png"))

image_list = [img1, img2, img3]

my_label = Label(root, image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def forwardImage(img_num):
    global my_label
    global nextBtn
    global backBtn
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    nextBtn.grid_forget()
    backBtn.grid_forget()

    backBtn = Button(root, text="Back", bg="green", fg="#fff", command=lambda : backwardImage(img_num-1))
    backBtn.grid(row=1, column=0, pady=10)

    nextBtn = Button(root, text="Next", bg="green", fg="#fff", command=lambda: forwardImage(img_num+1))
    if img_num == 2:
        nextBtn = Button(root, text="Next", state=DISABLED, bg="green", fg="#fff", command=lambda: forwardImage(img_num+1))
    nextBtn.grid(row=1, column=2)

def backwardImage(img_num):
    global my_label
    global nextBtn
    global backBtn
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    nextBtn.grid_forget()
    backBtn.grid_forget()

    backBtn = Button(root, text="Back", bg="green", fg="#fff", command= lambda : backwardImage(img_num-1))
    if img_num == 0:
        backBtn = Button(root, text="Back", state=DISABLED, bg="green", fg="#fff", command=lambda: backwardImage(img_num))
    backBtn.grid(row=1, column=0, pady=10)

    nextBtn = Button(root, text="Next", bg="green", fg="#fff", command=lambda: forwardImage(img_num + 1))
    if img_num == 2:
        nextBtn = Button(root, text="Next", state=DISABLED, bg="green", fg="#fff",
                         command=lambda: forwardImage(img_num + 1))
    nextBtn.grid(row=1, column=2)


backBtn = Button(root, text="Back", state=DISABLED, bg="green", fg="#fff", command=backwardImage)
backBtn.grid(row=1, column=0, pady=10)
Button(root, text="Close Program", bg="red", fg="#fff", command=root.quit).grid(row=1, column=1)
nextBtn = Button(root, text="Next", bg="green", fg="#fff", command=lambda : forwardImage(1))
nextBtn.grid(row=1, column=2)


root.mainloop()