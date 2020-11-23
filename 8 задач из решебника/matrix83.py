a = []
x = 0
b = []
M = int(input("Введите M: "))
s = 0
for i in range(M):
    a.append([])
    for j in range(M):
        a[i] += [int(input())]
print(a)
for i in range(M):
    for j in range(M):
        if i+j == s:
            s+=1
            x+=a[i][j]
    print(x)
    x = 0