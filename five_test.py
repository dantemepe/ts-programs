import time
import os
d1 = ""
d2 = ""
d3 = ""
d4 = ""
d5 = ""
x1d = False
x2d = False
x3d = False
x4d = False
x5d = False
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
att = 0
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ACH = False
len5 = False
while not len5:
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
    while x1d == False:
        if ALF[x1] == ANS[0]:
            x1d = True
            d1 = ANS[x1]
        x1 += 1
        att +=1
    while x2d == False:
        if ALF[x2] == ANS[1]:
            x2d = True
            d2 = ANS[x2]
        x2 += 1
        att +=1
    while x3d == False:
        if ALF[x3] == ANS[2]:
            x3d = True
            d3 = ANS[x3]
        x3 += 1
        att +=1
    while x4d == False:
        if ALF[x4] == ANS[3]:
            x4d = True
            d4 = ANS[x4]
        x4 += 1
        att+=1
    while x5d == False:
        if ALF[x5] == ANS[4]:
            x5d = True
            d5 = ANS[x5]
        x5 += 1
        att +=1
    char = d1+d2+d3+d4+d5

    print(char, str(att))
    if char == ANS:
        print("Success! It took",str(att),"attempts to get your 5 character combination")
        ACH = True