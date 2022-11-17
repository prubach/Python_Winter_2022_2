d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}
print(d1)
d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Jan': 'Enero'}
print(d1)

print(d1['Feb'])
d1['Apr'] = 'April'
print(d1)
d1['Apr'] = 'Aprilo'
print(d1)

for k in d1.keys():
    print(f'{k}: {d1[k]}')
print('-----------')

for v in d1.values():
    print(f'{v}')
print('-----------')

t1 = (3543, 262)
t11, t12 = t1
print(t11)

print('-----------')
for k, v in d1.items():
    print(f'{k}: {v}')
