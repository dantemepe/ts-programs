from tkinter import *
import random
import time

# ask for goal
goal = int(input("How many windows you wanna close?? "))

root = Tk()
root.withdraw()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

start_time = time.time()
hits = 0

def spawn_target():
    global hits

    win = Toplevel()
    win.geometry("50x50")

    # random position
    x = random.randint(0, screen_w - 80)
    y = random.randint(0, screen_h - 80)
    win.geometry(f"50x50+{x}+{y}")

    def hit():
        global hits
        hits += 1
        win.destroy()

        if hits >= goal:
            end = time.time()
            print(f"took you {end - start_time:.2f} seconds")
            root.destroy()
        else:
            spawn_target()

    btn = Button(win, text="CLICK", command=hit)
    btn.pack(expand=True, fill="both")

# start with 1 target
spawn_target()

root.mainloop()