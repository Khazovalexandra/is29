a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))

if (a<b) and (b<c):
    a *=2
    b *=2
    c *=2
else:
    a*=-1
    b *= -1
    c *= -1
print(a, b, c)