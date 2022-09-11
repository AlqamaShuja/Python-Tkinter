from tkinter import *
root = Tk()

# frame1 = LabelFrame(root, text="Hello", pady=10, padx=10)
# frame1.pack(padx=10, pady=10)

# btn1 = Button(frame1, text="Click me")
# btn1.pack(side=LEFT, fill=Y)

frame2 = Frame(root, bg="green", pady=10, padx=10)
frame2.pack(side=TOP, fill=X, padx=10, pady=10)

btn2 = Button(frame2, text="Dont Click me")
btn2.pack(side=TOP)

frame3 = Frame(root, bg="red")
frame3.pack(side=BOTTOM, fill=X)
btn3 = Button(frame3, text="Hey smart",)
btn3.pack()

frame4 = Frame(root, bg="yellow")
frame4.pack(side=TOP, fill=X)
btn4 = Button(frame4, text="Hey smart", bg="black", fg="white")
btn4.pack()


root.mainloop()