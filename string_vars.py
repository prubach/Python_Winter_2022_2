s1 = 'abcdefgfgh'
print(len(s1))
print(s1[0])
print(s1[2])
print(s1[2:6])
print(s1[2:])
print(s1[:2])
print(s1[-2:])
s2 = s1[:2] + s1[-2:]
print('s2: {}'.format(s2))

print(s1.find('fg'))