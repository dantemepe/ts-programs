import keyboard
import time
import threading
import sys

running = True
pos = 0
dire = 1

bar = "•••••••===▮===•••••••"
length = len(bar)

def listen_key():
    global running
    keyboard.read_key()
    running = False

threading.Thread(target=listen_key, daemon=True).start()


print(bar)
print(" " * length)

while running:
    sys.stdout.write("\033[F")
    sys.stdout.write(" " * length + "\r")
    sys.stdout.write(" " * pos + "^\n")
    sys.stdout.flush()

    pos += dire
    if pos <= 0 or pos >= length - 1:
        dire *= -1

    time.sleep(0.04)
 #TIKI TIKI TIIKIIIIIIII MATETEKITANAAAAAAAA TIKI TIKI TIKI TIKI TIIIIIII

cent = length // 2
if abs(pos - cent) <= 1:
    print("PERFECT!")
elif abs(pos - cent) <= 3:
    print("good")
else:
    print("miss")
input("")