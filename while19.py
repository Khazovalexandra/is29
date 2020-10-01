n = int(input("Введите число: "))
x = 0

while n>0:
    x = x * 10 + n%10
    n = n//10
print(x)