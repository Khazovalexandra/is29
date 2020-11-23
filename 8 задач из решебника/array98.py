a = []
b = []
n = int(input("Введите число элелентов массива: "))
for i in range(n):
    a.append(int(input("Ввод массива: ")))
for i in a:
    k = 0
    for j in a:
        if i==j:
            k+=1

    if k>=3:
        b.append(i)

print(b)