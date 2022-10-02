import threading
import time

def main_function():
    global continuer_global, i
    i = 0
    t1 = threading.Thread(target = counter)
    t1.daemon = True # With this parameter, the thread functions stops when you stop the main program
    t1.start()
    print("Here you can do other stuff")
    input("Press Enter to exit program\n")

def counter ():
    # Do an action in parallel
    global i
    while True:
        print("i =", i)
        i += 1
        time.sleep(1)

main_function()