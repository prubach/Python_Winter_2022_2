#a = 5

for i in range(4):
    print(f'i={i}')
    a = 7
    print(f'a={a}')

print('------')
print(f'i={i}')
print(f'a={a}')

b = 11
c = 1
a = 2

if a > 6:
    if b < 10:
        d = 463
    else:
        d = 346

#print(f'd={d}')
print('d={}'.format(d))
print('d=' + str(d))
