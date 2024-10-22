#1
# with open('fisier.txt', 'r') as fisier:
#     phrase = fisier.read()

# letters = "abcdefghijklmnopqrstuvwxyz"
# freq = {}

# for letter in letters:
#     freq[letter] = phrase.count(letter)

# maximum = max(freq.values())

# matrix = []

# for i in range(26):
#     matrix += ['.' * (maximum - freq[chr(ord('a') + i)]) + 'o' * freq[chr(ord('a') + i)]]

# for j in range(26):
#     for i in range(maximum):
#        print(matrix[i][j])

#2
print([(letter, ord(letter), 25 - index) for index, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])

#3
hexadecimals = '0123456789ABCDEF'
with open(r'D:\desktop folders\facultate\python\labs\fisier.txt', 'r') as fisier:
    text = fisier.read()

hexa = [[]]
for i in range(16):
    hexa[0].append('0' + hexadecimals[i])

for i in range(len(text) // 16):
    hexa.append([hex(ord(text[i * 16 + index])) for index in range(16)])
hexa.append([hex(ord(text[i * 16 + index])) for index in range(16 - len(text) % 16)])

aux = [[f"{elem[2:]:>02}" for elem in line] for line in hexa]

result = []
for line in aux:
    print(' '.join(line))
    
