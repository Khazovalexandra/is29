a = []
n = int(input("Введите число элементов массива: "))
for i in range(n):
    a.append(int(input('Ввод массива: ')))
min = 1000000000
max = 0
k = 0
j = 0
for i in range(n):
    if a[i]>max:
        max = a[i]
        k = i+1
    if a[i]<min:
        min = a[i]
        j = i+1
print('Номер минимального -  ', j)
print('Номер максимального - ', k)
