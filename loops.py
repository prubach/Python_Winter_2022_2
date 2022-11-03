v = 0
for i in range(5):
    print(f'i={i}')
    v = v + 1

print(f'v={v}')

print('-------------')
for i in range(1, 5):
    print(f'i={i}')

print('-------------')
for i in reversed(range(-5, 10, 2)):
    print(f'i={i}')

print('-------------')
j = 0
# while j < 7:
#     j += 1
#     if j == 3:
#         continue
#     if j == 5:
#         break
#     print(f'j={j}')

while True:
    j += 1
    if j == 3:
        continue
    if j == 5:
        break
    print(f'j={j}')