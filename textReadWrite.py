from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry("500x500")

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="E:\Code\Python\practice_121", title="Open File", filetypes=(("text files", "*.txt"),))
    text_file = open(text_file, "r")
    stuff = text_file.read()
    myText.insert(END, stuff)
    text_file.close()

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="E:\Code\Python\practice_121", title="Open File",
                                           filetypes=(("text files", "*.txt"),))
    text_file = open(text_file, "w")
    text_file.write(myText.get(1.0, END))

myText = Text(root, width=40, height=10, font=("helvatica", 16))
myText.pack(pady=20)

open_btn = Button(root, text="Open file", command=open_txt)
open_btn.pack(pady=20)

open_btn = Button(root, text="Save file", command=save_txt)
open_btn.pack(pady=20)












root.mainloop()