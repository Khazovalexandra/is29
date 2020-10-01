n = int(input("Введите число: "))
x = 1

for i in range(2, n+1):
    x *=i
print("N!=", x)