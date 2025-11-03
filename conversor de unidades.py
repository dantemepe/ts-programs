import time
import sys
def exiting():
    time.sleep(6.7)
    print("PRESIONAR CUALQUIER TECLA PARA CERRAR PROGRAMA")
    exi = input("")
    sys.exit()
print("CONVERTIDOR DE UNIDADES")
print("TIPOS DE UNIDAD: KG, HG, DAG, G, DG, CG, MG")
pn = input("TIPO DE PRIMERA UNIDAD  > ")
unt = input("CANT. DE PRIMERA UNIDAD  > ")
sn = input("TIPO DE SEGUNDA UNIDAD  > ")
if pn.lower() == "kg":
    if sn.lower() == "kg":
        print(str(unt),"kg.")
    elif sn.lower() == "hg":
        print(str(float(unt)*10),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)*100),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)*1000),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)*10000),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*100000),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*1000000),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "hg":
    if sn.lower() == "kg":
        print(str(float(unt)/10),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)*1),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)*10),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)*100),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)*1000),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*10000),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*100000),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "dag":
    if sn.lower() == "kg":
        print(str(float(unt)/100),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)/10),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)*1),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)*10),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)*100),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*1000),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*10000),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "g":
    if sn.lower() == "kg":
        print(str(float(unt)/1000),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)/100),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)/10),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)*1),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)*10),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*100),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*1000),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "dg":
    if sn.lower() == "kg":
        print(str(float(unt)/10000),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)/1000),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)/100),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)/10),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)*1),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*10),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*100),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "cg":
    if sn.lower() == "kg":
        print(str(float(unt)/100000),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)/10000),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)/1000),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)/100),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)/10),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)*1),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*10),"mg.")
        exiting()
    else:
        print("Error!")
        print("CERRANDO PROGRAMA...")
        time.sleep(1)
        sys.exit(0)
elif pn.lower() == "mg":
    if sn.lower() == "kg":
        print(str(float(unt)/1000000),"kg.")
        exiting()
    elif sn.lower() == "hg":
        print(str(float(unt)/100000),"hg.")
        exiting()
    elif sn.lower() == "dag":
        print(str(float(unt)/10000),"dag.")
        exiting()
    elif sn.lower() == "g":
        print(str(float(unt)/1000),"g.")
        exiting()
    elif sn.lower() == "dg":
        print(str(float(unt)/100),"dg.")
        exiting()
    elif sn.lower() == "cg":
        print(str(float(unt)/10),"cg.")
        exiting()
    elif sn.lower() == "mg":
        print(str(float(unt)*1),"mg.")
        exiting()
    else:
        print("Error!")
        time.sleep(1)
        print("CERRANDO PROGRAMA...")
        sys.exit(0)
else:
    print("Error!")
    print("CERRANDO PROGRAMA...")
    time.sleep(1)
    sys.exit(0)
