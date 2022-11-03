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

#print('abc\ndefe\tgfvbhehe')
print('abc\\ndefe\\tgfvbhehe')
print('a\'bc\\ndefe\\tgfv"bhe"he')
print("a'bc\ndefe\\tgfv\"bhe\"he")
print('łóżżąąśćśćfqfeqgf')
print(ord('a'))
print(ord('ł'))
print(chr(98))
