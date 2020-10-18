f = open('123.txt')
a = int(f.read(1))
b = int(f.read(2))
c = int(f.read(3))

if (a < b) and (b < c):
    a *= 2
    b *= 2
    c *= 2
else:
    a *= -1
    b *= -1
    c *= -1

print(a,b,c)
f.close()

f = open('a,b,c', 'w')
f.write(str(a))
f.write(str(b))
f.write(str(c))
f.close()