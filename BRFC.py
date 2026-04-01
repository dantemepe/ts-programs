lschr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #0 - 51
import os
import time
import random
spinner = str(r"|/-\|")
spin_i = 0
l_upd = time.time()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
 spw = input("enter a 6 character secret password for it to guess(or generate a random one inputting ?): ")
 if len(spw) == 6:
  break
 elif spw == "?":
   spw = lschr[random.randint(0,51)]+lschr[random.randint(0,51)]+lschr[random.randint(0,51)]+lschr[random.randint(0,51)]+lschr[random.randint(0,51)]+lschr[random.randint(0,51)]
   print("password is "+spw)
   break
 else:
   print("dude that's not 6 characters, that is",len(spw),"characters, and it needs to be 6")
   time.sleep(3.5)
   clear()
gspwo = [ 0, 0, 0, 0, 0, 0 ]  # lista guesspassword con cada caracter de las seis letras como un numero para despues que cada uno se cambie y se le asigne un caracter
att = 0
while True:
  att +=1
  gst = ""                    # establece un string vacio para despues añadirle caracteres
  for i in gspwo:             # por cada caracter que hay en guesspasword:
    gst += lschr[i]           #  se le añade al string guesstotal el caracter correspondiente al valor del numero de la lista en el que esta (ej. esta en el quinto loop y se le añade esto y el valor del quinto caracter de la lista es 25, se le va a añadir z)
  if att % 123456 == 0:
        spin_i += 1
        print("\rTrying:", gst, spinner[spin_i % 4], "Attempts:", att, end="")


  if gst == spw:
    clear()
    print("Done, guessed in "+str(att)+" attempts")
    break
  gspwo[5] +=1
  if gspwo[5] > 51:
    gspwo[5] = 0
    gspwo[4] += 1
  if gspwo[4] > 51:
    gspwo[4] = 0
    gspwo[3] +=1
  if gspwo[3] > 51:
    gspwo[3] = 0
    gspwo[2] +=1
  if gspwo[2] > 51:
    gspwo[2] = 0
    gspwo[1] +=1
  if gspwo[1] > 51:
    gspwo[1] = 0
    gspwo[0] +=1
  if gspwo[0] > 51:
    print("Exhausted all combinations")
    break