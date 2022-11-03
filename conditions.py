p = True
q = False

if p:
    print('p is True')
else:
    print('p is not True')

if not p:
    print('p is not True')
else:
    print('p is True')

print('----')
if p and q:
    print('p and q are True')
else:
    print('p and q are not True')

print('----')
if p or q:
    print('p or q are True')
else:
    print('p or q are not True')

print('----')
if p ^ q:
    print('p xor q are True')
else:
    print('p xor q are not True')

print('----')
#v = None
v = ''
if v:
    print(f'v={v}')
else:
    print('not v')

t = '5aav'
tt = t + v
print(tt)

print('-----')

w = 11.5
print(type(w))
z = 11
print(type(z))

if w >= z:
    print('w >= z')
else:
    print('not w >= z')

if w == z:
    print('w = z')
else:
    print('w != z')

y = 10 if w == 11 else 50
print(f'y={y}')
print('y={}'.format(y))
print('y=' + str(y))