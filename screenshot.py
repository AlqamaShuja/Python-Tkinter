# install mss
from tkinter import *
from mss import mss
import time
import threading
from random import randint

root = Tk()
root.geometry("500x500")

def mainFunc():
    t1 = threading.Thread(target=screenShot)
    t1.daemon = True
    t1.start()
    print("Preparing for screenshot")

def screenShot():
    # time.sleep(3)
    time.sleep(3)
    with mss() as screen_shot:
        filename = "ss_" + str(randint(0, 999999) * 2) + str(randint(999999, 100000000) * 2) + ".png"
        screen_shot.shot(output=filename)
        lbl.config(text="Screen shot has been saved")

btn = Button(root, text="Take Screenshot", command=mainFunc)
btn.pack(pady=20)

lbl = Label(root, text="")
lbl.pack(pady=10)





root.mainloop()