import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

wfn = 0  # first number placeholder
wot = "+"
wsn = 0
clear()
print("Calc file recode!")
listofots = ["+","-","x","√","/","^","1","2","3","4","5","6","addition","subtraction","multiplication","division","exponent","square root"]
import time
time.sleep(3.5)
clear()

while True:
 fn = input("Input first number  > ")
 try:
  wfn = int(fn) 
  break  
 except ValueError:
  try:
   wfn = float(fn) 
   break  
  except ValueError:
   print("Error, please enter a valid number!")
while True:
 print(" ")
 print("First number =",fn," Operation type = ?  Second number = ?")
 ot = input("Enter operation type (type ? to see all operation types)  > ")
 if ot == "?":
    clear()
    print("_____________________________________________________________________")
    print("|                                                                   |")
    print("| Operation types:                                                  |")
    print("|  (1) Addition(+)     (2) Subtraction(-)    (3) Multiplication(x)  |")
    print("|  (4) Divission(/)    (5) Exponent(^)       (6) Square root(√)     |")
    print("|                                                                   |")
    print(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅")
    print(" ")
    print(" ")
 if ot.lower() not in listofots:
    print("operation not recognized")
 else:
    break
while True:
 print(" ")
 print("First number =",fn," Operation type =",ot," Second number = ?")
 sn = input("Input Second Number  > ")
 try:
  wsn = int(sn) 
  break 
 except ValueError:
  try:
   wsn = float(sn)  
   break  
  except ValueError:
   print("Error, please enter a valid number!")
import random

for _ in range(random.randint(6,9)):
    for dots in [".", "..", "..."]:
        print(f"Calculating{dots}")
        time.sleep(0.15)
        clear()
