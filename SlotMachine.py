print("slot machine idk")
import random
import sys
import os
import time

money = 150
loans = 3
firstSpin = True

x = y = z = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dispmoney():
    print("$" + str(money))

def randomnums():
    global x, y, z
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    z = random.randint(0, 9)

def smascii():
    print("      _______")
    print("  ___|  BIG  |___")
    print("__|_____WIN_____|__")
    print("|  ___  ___  ___  | _-_")
    print("| |   ||   ||   | | OOI")
    print(f"| | {x} || {y} || {z} | | ||")
    print("| |___||___||___| | I")
    print("|                 |I1")
    print("|   ___________   |")
    print("|  |  JACKPOT  |  |")
    print("|   ¯¯¯¯¯¯¯¯¯¯¯   |")
    print("|                 |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
def animate_spin():
    global x, y, z

    delays = [0.07, 0.095, 0.1, 0.115, 0.13, 0.165, 0.2]
    for d in delays:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = random.randint(0, 9)

        clear()
        smascii()
        dispmoney()
        time.sleep(d)

while True:
    clear()

    if firstSpin:
        dispmoney()
        start = input("Play the slot machine? (costs $10) (y/n): ").lower()
        if start == 'n':
            sure = input("Are you sure? (y/n): ").lower()
            if sure == "y":
                print("Goodbye!")
                sys.exit()
            else:
                continue
        firstSpin = False

    if money < 10:
        print("\nYou ran out of money!")
        if loans == 0:
            print("You lose!")
            time.sleep(1)
            sys.exit()
        loanaccept = input(f"Take a loan? ({loans} left) y/n: ").lower()
        if loanaccept == "y":
            print("Bank gives you $150")
            loans -= 1
            money += 150
            time.sleep(1)
        else:
            print("You lose!")
            time.sleep(1)
            sys.exit()

    money -= 10
    animate_spin()
    randomnums()
    clear()
    smascii()
    dispmoney()

    winmsg = ""

    if x == y == z == 7:
        winmsg = " JACKPOT!! "
        money *= 2
    elif x == y == z:
        winmsg = "Three equal special!"
        money = int(money * 1.65)

    if winmsg:
        print(winmsg)
        dispmoney()

    nextmove = input("\nSpin again? (y/n): ").lower()
    if nextmove == 'n':
        print("Goodbye!")
        time.sleep(1)
        sys.exit()
