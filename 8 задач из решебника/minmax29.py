a = []
i = 0
n = int(input("Введите число элементов массива: "))
for i in range(n):
    a.append(int(input('Ввод массива: ')))
min = 1000000000
k =  1
maxk = 1
for i in range(n):
    if a[i]<min:
        min = a[i]

for i in range(n-1):
    if k>maxk:
        maxk = k
    if (a[i] == min) and (a[i] == a[i+1]):
        k = k+1

print(maxk)
