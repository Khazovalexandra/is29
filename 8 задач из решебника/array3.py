array = []
n = int(input("Введите число большее 1: "))
A = int(input("Введите первый член арифметической прогрессии: "))
D = int(input("Введите разность арифметической прогресии: "))
k = 0
for i in range(n):
    x = A + k*D
    k = k+1
    array.append(x)
print(array)

