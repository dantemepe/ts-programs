X = True
Y = True
Z = True

Ascii = ()
def Ascii():
 print(" _____________________") 
 time.sleep(0.45)
 print("|  _________________  |")
 time.sleep(0.45)
 print("| |        "+str(rst)+"        | |")
 time.sleep(0.45)
 print("| |_________________| |")
 time.sleep(0.45)
 print("|  ___ ___ ___   ___  |")
 time.sleep(0.45)
 print("| | 7 | 8 | 9 | | + | |")
 time.sleep(0.45)
 print("| |___|___|___| |___| |")
 time.sleep(0.45)
 print("| | 4 | 5 | 6 | | - | |")
 time.sleep(0.45)
 print("| |___|___|___| |___| |")
 time.sleep(0.45)
 print("| | 1 | 2 | 3 | | x | |")
 time.sleep(0.45)
 print("| |___|___|___| |___| |")
 time.sleep(0.45) #                  -https://ascii.co.uk/art/calculator
 print("| | . | 0 | = | | / | |")
 time.sleep(0.45)
 print("| |___|___|___| |___| |")
 time.sleep(0.45)
 print("|_____________________|")

 time.sleep(0.7)
 print(" ")

import sys
print("calculator made by dante") #disclaimer
import time #imports time (lets you use time.sleep which makes you able to make the user wait time for other part of code to run)
time.sleep(1) #wait
print(" ") #space
time.sleep(0.5) # wait
print(" ") #space
time.sleep(0.25) #wait
fn = input("Enter first number:  ") #asks you the first number for the operation
try:
  fnr = float(fn)                        #tries to convert the number to a readable number for python
except:
 print (" Error! ")                      #Closes code if wrong
 print (" ")
 while X == True:
  time.sleep(0.1)
  C = input("Press C to close this window  > ")
  if C == ("C"):
    X = False
    break
  else:
    pass
  if C == ("c"):
    X = False
    break
  else:
    pass   

time.sleep(0.3) #wait
print(" ") #  S P A C E
print("types of operations:")    #
print(" 1.  Addition(+)")        #
print(" 2.  Difference(-)")      # Informs you of which operations you can do
print(" 3.  Multiplication(x)")  #
print(" 4.  Division(/)")        #
print(" 5.  Power(^)")           #
ot = input("type of operation:  ") #asks the user what kinda operation you wanna do
try:
   strot = int(ot) #converts the type of operation to a number so that python can identify it as one
except:
 print (" Error! ")                      #Closes code if wrong
 print (" ")
 while X == True:
  time.sleep(0.1)
  C = input("Press C to close this window  > ")
  if C == ("C"):
    X = False
    break
  else:
    pass
  if C == ("c"):
    X = False
    break
  else:
    pass
time.sleep(0.3) #waits

print(" ") #  S P A C E
if strot == 1: print("Addition(+)")        #
if strot == 2: print("Difference(-)")      #
if strot == 3: print("Multiplication(x)")  # checks what option you chose, and tells you
if strot == 4: print("Division(/)")        #
if strot == 5: print("Power(^)")           #
print(" ") #space
time.sleep(0.35) #wait
sn = input("Enter second number:  ") #makes you insert the second number
try:
  snr = float(sn) #converts the second number so that python can read it as a number and not text
except:
  print("Not a valid number! Try again") #
  time.sleep(1.5)                        #
  sys.exit(0)                            #closes the code
time.sleep(0.3) #waits
rst = ("Error!") #makes the rst variable exist

if strot == 1: rst = (fnr)+(snr)  #
if strot == 2: rst = (fnr)-(snr)  #
if strot == 3: rst = (fnr)*(snr)  # all of ts just does the maths
if strot == 4: rst = (fnr)/(snr)  #
if strot == 5: rst = (fnr)**(snr) #
time.sleep(0.5) #waits
print(" ") #makes space
if rst == ("Error!"):
 print (" Error! ")
 print (" ")
while rst == ("Error!"):
  time.sleep(0.1)
  C = input("Press C to close this window  > ")
  if C == ("C"):
    rst = ("Error!")
    sys.exit(0)
  else:
    pass
  if C == ("c"):
    rst = ("Error!")
    sys.exit(0)
  else:
    pass

print("result =  "+str(rst)) #shows result


time.sleep(5.5) #waits
print(" ") #makes_space
qtn =  input("yo wanna check out this cool calc?? (Y/N)  > ") #asks the user if they wanna see a cool calc ascii
if qtn == str("Y"): #checks if the user responded by saying true or false
 Ascii()
if qtn == str("y"): #checks if the user responded by saying true or false
 Ascii()
else:
 print("oh ok") #doesnt show the calc ascii ):
 time.sleep(0.7)
 print(" ")
while X == True:
  time.sleep(0.1)
  C = input("Press C to close this window  > ")
  if C == ("C"):
    X = False
    break
  else:
    pass
  if C == ("c"):
    X = False
    break
  else:
    pass
