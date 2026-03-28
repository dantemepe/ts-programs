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
x6d = False
x7d = False
x8d = False
x9d = False
x10d = False
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
att = 0
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ACH = False
len5p = False
while not len5p:
    ANS = input("Please input any 5+ character combination  > ")
    length = len(ANS)
    if length >= 5:
        len5p = True
    else:
        print("Please actually enter a 5+ character combination")
        time.sleep(2.67)
        clear()
        continue
while ACH == False:
    att = att+1
    while x1d == False:
        if ALF[x1] == ANS[0]:
            x1d = True
            d1 = ALF[x1]
        x1 += 1
        att +=1
    while x2d == False:
        if ALF[x2] == ANS[1]:
            x2d = True
            d2 = ALF[x2]
        x2 += 1
        att +=1
    while x3d == False:
        if ALF[x3] == ANS[2]:
            x3d = True
            d3 = ALF[x3]
        x3 += 1
        att +=1
    while x4d == False:
        if ALF[x4] == ANS[3]:
            x4d = True
            d4 = ALF[x4]
        x4 += 1
        att+=1
    while x5d == False:
        if ALF[x5] == ANS[4]:
            x5d = True
            d5 = ALF[x5]
        x5 += 1
        att +=1
    char = d1+d2+d3+d4+d5
    if len(ANS) == 6:
        while x6d == False:
            if ALF[x6] == ANS[6]:
                x6d = True
                d6 = ALF[x6]
            x6 += 1
            att +=1
            char = d1+d2+d3+d4+d5+d6
    
    elif len(ANS) == 7:
        while x6d == False:
            if ALF[x6] == ANS[5]:
                x6d = True
                d6 = ALF[x6]
            x6 += 1
            att +=1
        while x7d == False:
            if ALF[x7] == ANS[6]:
                x7d = True
                d7 = ALF[x7]
                char = d1+d2+d3+d4+d5+d6+d7
            x7 += 1
            att +=1

    elif len(ANS) == 8:
        while x6d == False:
            if ALF[x6] == ANS[5]:
                x6d = True
                d6 = ALF[x6]
            x6 += 1
            att +=1
        while x7d == False:
            if ALF[x7] == ANS[6]:
                x7d = True
                d7 = ALF[x7]
            x7 += 1
            att +=1
        while x8d == False:
            if ALF[x8] == ANS[7]:
                x8d = True
                d8 = ALF[x8]
                char = d1+d2+d3+d4+d5+d6+d7+d8
            x8 += 1
            att +=1
            
    elif len(ANS) == 9:
        while x6d == False:
            if ALF[x6] == ANS[5]:
                x6d = True
                d6 = ALF[x6]
            x6 += 1
            att +=1
        while x7d == False:
            if ALF[x7] == ANS[6]:
                x7d = True
                d7 = ALF[x7]
            x7 += 1
            att +=1
        while x8d == False:
            if ALF[x8] == ANS[7]:
                x8d = True
                d8 = ALF[x8]
            x8 += 1
            att +=1
        while x9d == False:
            if ALF[x9] == ANS[8]:
                x9d = True
                d9 = ALF[x9]
                char = d1+d2+d3+d4+d5+d6+d7+d8+d9
            x9 +=1
            att +=1
    
    elif len(ANS) == 10:
        while x6d == False:
            if ALF[x6] == ANS[5]:
                x6d = True
                d6 = ALF[x6]
            x6 += 1
            att +=1
        while x7d == False:
            if ALF[x7] == ANS[6]:
                x7d = True
                d7 = ALF[x7]
            x7 += 1
            att +=1
        while x8d == False:
            if ALF[x8] == ANS[7]:
                x8d = True
                d8 = ALF[x8]
            x8 += 1
            att +=1
        while x9d == False:
            if ALF[x9] == ANS[8]:
                x9d = True
                d9 = ALF[x9]
            x9 +=1
            att +=1
        while x10d == False:
            if ALF[x10] == ANS[9]:
                x10d = True
                d10 = ALF[x10]
                char = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10
            x10 +=1
            att +=1
    print(char, str(att))
    if char == ANS:
        print("Success! It took",str(att),"attempts to get your 5+ character combination")
        ACH = True