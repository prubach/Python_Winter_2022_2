a = 35
b = 3.556
print(a)
print(type(a))
print(b)
print(type(b))
#c = a + int(b)
c = a + round(b)
print(c)
print(type(c))

print('------------')
d = 23738357345321641565465462356723575734724725727316741512452145
print(d)
e = d + 1
print(e)

f = 23738357345321641565465462356723575734724725727316741512452145.6
print(f)
g = f + 1010000
print(g)

h = 0.00000000000000000000000000000444434242
print(h)

i = 1.79e308
print(i)
i = 1.8e308
print(i)

print('-------------')
bb = 0b101
print(bb)
hx = 0x1a
print(hx)
print('-------------')
j = 2000
k = 50
print(j/k)
print(type(j/k))
k = 5
h = k**3
print(h)
g = 12
print(g % 8)

s1 = '23'
s2 = '25.2525'
print(s1.isnumeric())
a = int(s1)
b = float(s2)
print(a + b)

print(round(b, 2))