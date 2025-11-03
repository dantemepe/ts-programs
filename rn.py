import math
import time
import sys

def main():
    print("recta numerica")

    # Primer número
    try:
        fn = float(input("INGRESAR PRIMER NUMERO  > "))
    except ValueError:
        print("Número inválido :(")
        time.sleep(0.7)
        sys.exit(0)
    print(fn)

    # Espacios
    try:
        btwn = int(input("INGRESAR ESPACIOS ENTRE PRIMER Y SEGUNDO NUMERO  > "))
        if btwn <= 0:
            raise ValueError
    except ValueError:
        print("Número de espacios inválido :P")
        time.sleep(0.7)
        sys.exit(0)
    print(btwn)

    # Segundo número
    try:
        sn = float(input("INGRESAR SEGUNDO NUMERO  > "))
    except ValueError:
        print("Número inválido :(")
        time.sleep(0.7)
        sys.exit(0)
    print(sn)
    print("")

    # Cálculos
    try:
        ol = sn - fn
        divol = ol / btwn
    except Exception as e:
        print("Error en el cálculo:", e)
        sys.exit(0)

    print("El valor de un espacio es", divol)

    x = 0
    for i in range(btwn):
        x += 1
    x -= 1

    print("...|  |", str(fn), x * " | " + str(sn), "|  |...")

    time.sleep(2)
    input("PRESIONAR ENTER PARA CERRAR PROGRAMA")
    sys.exit()

if __name__ == "__main__":
    main()
