import random
import time
import os
att = 0
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
ALF = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6","7","8","9"
ACH = False
len5 = False
while len5 == False:
    ANS = input("Please input any 5 character combination  > ")
    length = len(ANS)
    if length == 5:
        len5 = True
    else:
        print("Please actually enter a 5 character combination")
        time.sleep(2.67)
        clear()
        continue
while ACH == False:
    att = att+1
    x1 = random.randint(0,61)
    x2 = random.randint(0,61)
    x3 = random.randint(0,61)
    x4 = random.randint(0,61)
    x5 = random.randint(0,61)
    char= ALF[x1]+ALF[x2]+ALF[x3]+ALF[x4]+ALF[x5]
    print(char, str(att))
    if char == ANS:
        print("Success! It took",str(att),"attempts to get your 5 character combination")
    else:
        pass
