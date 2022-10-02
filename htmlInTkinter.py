# install requests
# install tkhtmlview
from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.geometry("500x500")

my_label = HTMLLabel(root, html="Hello")
my_label.pack(pady=20)

my_link1 = HTMLLabel(root, html="<a href='https://www.google.com' style='color:green; text-decoration: none'>Hello</a>")
my_link1.pack()







root.mainloop()