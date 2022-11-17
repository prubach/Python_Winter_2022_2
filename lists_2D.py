l1 = [[1, 6, 7],
      [8, 9, 3],
      [7, 6, 2]]
print(l1)
l1_0 = l1[0]
l1_1 = l1[1]
l1_2 = l1[2]
print(l1_1[2])
print(l1[1][2])


print('--------------')
#TODO sum rows in l1
for i in range(len(l1)):
    print(sum(l1[i]))
print('--------------')

row_sum = []
for row in l1:
    print(sum(row))
    row_sum.append(sum(row))

print(row_sum)

res = [sum(idx) for idx in l1]
print(res)

#TODO sum columns in l1


res = [sum(idx) for idx in zip(*l1)]
print(res)

#TODO sum all elements of l1
print(sum(res))

