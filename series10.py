k = 0
a = []
n = int(input("Введите число: "))
for i in range(n):
    a.append(int(input("Ввод массива: ")))

for i in range(n):
    if a[i]%2 == 0:
        k +=1
if k!=0:
    print(True)
else:
    print(False)