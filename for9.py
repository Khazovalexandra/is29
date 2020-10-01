a = int(input("Введите число: "))
b = int(input("Введите число: "))
x = 0

if a<b:
    for i in range(a, b+1):
        x = x+i*i
print(x)
