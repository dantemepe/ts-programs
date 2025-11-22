import math
import time
import sys
print("recta numerica")
fn = input("INGRESAR PRIMER NUMERO  > ")
print(fn)
btwn = input("INGRESAR ESPACIOS ENTRE PRIMER Y SEGUNDO NUMERO  > ")
print(btwn)
try:
    int(btwn)
except:
    print("Numero invalido :P")
    print("Cerrando terminal...")
    time.sleep(0.67)
    sys.exit(0)
sn = input("INGRESAR SEGUNDO NUMERO  > ")
print(sn)
print("")
ol = float(float(sn)-float(fn))
divol=str(ol/int(btwn))
print("El valor de un espacio es",divol)
x=0
for i in range(int(btwn)):
    x+=1
x-=1
print("...|  |",str(fn),x*" | "+str(sn),"|  |...")
time.sleep(2)
print("PRESIONAR ENTER PARA CERRAR PROGRAMA")
s=input("")
sys.exit()