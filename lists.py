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
python_string_index = l4[3].find("Python")
python_string = l4[3][python_string_index:python_string_index+6]
print(python_string)

#TODO sum up all numbers from l4  (type - check if it is a number)
sum_of_numbers = 0
for i in range(len(l4)):
    if type(l4[i])==int:
        sum_of_numbers += l4[i]
print(sum_of_numbers)

print('-----------')
l5 = [x for x in l4 if isinstance(x, (int, float, complex))]
print(l4)
print(l5)
print(sum(l5))

l6 = [x*3 for x in l5]
print(l6)

