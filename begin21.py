import math

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
x3 = int(input("Введите x3: "))
y3 = int(input("Введите y3: "))

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

per = a+b+c
p = int(per/2)

s = (p*(p-a)*(p-b)*(p-c))**0.5

print("p = ", per)
print("s = ", s)
