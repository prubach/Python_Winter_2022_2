t1 = (1413, 254346)
t2 = (2, 4, 6, 7)
print(t1[1])
print(t2[3])
#t1[1] = 24
t3 = t2[1:3]
print(t3)

print('--------')
l4 = [321, 26, 23163, 3267, 89, 26, 3267, 89]
print(l4)
s1 = set(l4)
print(s1)
# not possible to address an element of a set
#print(s1[3])
for el in s1:
    print(el)

l5 = list(s1)
print(l5)

