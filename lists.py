l1 = [321, 26, 23163, 3267, 89]
print(l1)
print(l1[1])
print(l1[1:4])
print(l1[-4:])

l1.append(765)
print(l1)
l1.insert(3, 989)
print(l1)
l1.remove(26)
print(l1)
l1.pop(4)
print(l1)

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')

l1.sort()
l1.sort(reverse=True)
for val in l1:
    print(f'val={val}')

l4 = [321, 26, 23163, 'Hello from Python 3', 3267, 89]
#TODO extract the "Python" string from the list l4
#TODO sum up all numbers from l4  (type - check if it is a number)
