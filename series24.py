a = []
n = int(input("Введите число: "))
for i in range(n):
    a.append(int(input("Ввод массива: ")))
s = 0
s0 = 0

for i in range(n):
    s = s + a[i]
    if a[i] == 0:
        s0 = s
        s = 0
print(s0)