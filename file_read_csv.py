my_file = 'my_matrix.csv'

m = []
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        r = []
        i += 1
        print(f'{i}: {line}', end='')
        for c in line.split(';'):
            #print(type(c))
            #print(c)
            r.append(int(c))
        m.append(r)

print(m)

