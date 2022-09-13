from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image
root = Tk()

img1 = ImageTk.PhotoImage(Image.open("images/image2.png"))
img1_label = Label(image=img1);
img1_label.pack()
root.iconphoto(False, img1)

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    # msg = simpledialog.askstring("Input", "Please Enter Fig-1, Fig-2")
    msg = messagebox.askretrycancel("Hello", "this message come from msgBox")
    Label(root, text=msg).pack()



Button(root, text="Show Pop Up Msg", command=popup).pack()





root.mainloop()