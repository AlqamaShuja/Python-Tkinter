from tkinter import *

root = Tk()
root.geometry("500x500")
mainMenu = Menu(root)
root.config(menu=mainMenu)


def newCommand():
    pass


file_menu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=file_menu)
file_menu.add_separator()

edit_menu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=edit_menu)
view_menu = Menu(mainMenu)
mainMenu.add_cascade(label="View", menu=view_menu)
file_menu.add_command(label="New", command=newCommand)
file_menu.add_command(label="Exit", command=root.quit)










root.mainloop()