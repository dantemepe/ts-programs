import math
import time

x = input("enter number to get the factorial of  > ")
try:
    xb = int(x)
except ValueError:
    print("Please enter a whole number.")
    raise SystemExit

def factorialshort():
    print("short way:")
    print(math.factorial(xb))
    print("")
    time.sleep(2)

def factorialmanual():
    if xb < 0:
        print("factorial not defined for negative numbers")
        return
    result = 1
    for i in range(2, xb + 1):
        result *= i
    print("long way:")
    print(result)
    print("")
    time.sleep(2)

print("a = short         b = long")
b = input("which way??  > ")
if b.lower() == "a":
    factorialshort()
elif b.lower() == "b":
    factorialmanual()
else:
    print("choose 'a' or 'b'")