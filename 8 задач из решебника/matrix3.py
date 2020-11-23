a = []
M = int(input("Введите M: "))
N = int(input("Введите N: "))
b = []
for i in range(M):
    b.append(int(input("Ввод массива: ")))
for i in range(M):
    a.append([b[i]])
    for j in range(N-1):
        a[i] += [int(b[i])]
print(a)