f = open('while.txt')
n =int(f.read())
x=0

while n > 0:
    x = x * 10 + n % 10
    n = n // 10
print(x)
f.close()

f = open('n=', 'w')
f.write(str(x))
f.close()