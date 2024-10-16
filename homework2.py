#1
def Fib(num):
    fib = [0, 1]

    if num <= 0:
        return []
    elif num == 1:
        return [0]

    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib

#2
def Primes(numbers):
    primes = []

    for num in numbers:
        if num % 2 != 0 or num == 2:
            if num == 0 or num == 1:
                continue
            elif num == 2:
                primes.append(num)
            else:
                for d in range(2, int(num / 2)):
                    if num % d == 0:
                        continue
            
                primes.append(num)
        
    return primes

#3
def Operations(a, b):

    intersection = []
    for item in a:
        if item in b:
            intersection.append(item)
    
    union = []
    for item in a:
        if item not in union:
            union.append(item)
    for item in b:
        if item not in union:
            union.append(item)
    
    a_minus_b = []
    for item in a:
        if item not in b:
            a_minus_b.append(item)
    
    b_minus_a = []
    for item in b:
        if item not in a:
            b_minus_a.append(item)

    return (intersection, union, a_minus_b, b_minus_a)            

#4
def Music(notes, moves, start):

    result = []
    result.append(notes[start])

    for move in moves:
        start = (start + move) % len(notes)
        result.append(notes[start])

    return result

#5
def MainDiagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = 0
    return matrix

#6
def Count(x, *lists):
    counts = {}
    result = []

    for list in lists:
        for item in list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

    for item, count in counts.items():
        if count == x:
            result.append(item)

    return result

#7
def Palindromes(nums):

    counter = 0
    greatest = None

    for num in nums:
        if str(num) == str(num)[::-1]:
            counter += 1
            if greatest is None or num > greatest:
                greatest = num
    
    return (counter, greatest)

#8
def ASCII(x = 1, strings = [], flag = True):
    result = []
    
    for string in strings:
        chars = []
        for char in string:
            if (ord(char) % x == 0) == flag:
                chars.append(char)
        result.append(chars)
    
    return result

#9
def Stadium(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        maximum = -1
        for row in range(rows):
            if matrix[row][col] <= maximum:
                result.append((row, col))
            else:
                maximum = matrix[row][col]
    return result

#10
def Lists(*lists):
    result = []
    maxlength = None
    for list in lists:
        if maxlength is None or maxlength < len(list):
            maxlength = len(list)
    
    for i in range(maxlength):
        tuple = []
        for list in lists:
            if i >= len(list):
                tuple.append(None)
            else:
                tuple.append(list[i])
        result.append(tuple)
    
    return result

#11
def Tuples(tuples):
    result = []

    while tuples:
        smallest = tuples[0]
        for item in tuples:
            if len(item[1]) >= 3 and len(smallest[1]) >= 3:
                if item[1][2] < smallest[1][2]:
                    smallest = item
            elif len(item[1]) < 3 and len(smallest[1]) >= 3:
                continue
            elif len(item[1]) < 3 and len(smallest[1]) < 3:
                continue
            elif len(item[1]) >= 3 and len(smallest[1]) < 3:
                smallest = smallest

        result.append(smallest)
        tuples.remove(smallest)

    return result
    

#12
def Rhymes(words):
    rhymes = {}

    for word in words:
        rhyme = word[-2:]
        if rhyme not in rhymes:
            rhymes[rhyme] = []
        rhymes[rhyme].append(word)
    
    return list(rhymes.values())

print(Fib(10)) #1
print(Primes([1, 2, 3, 4, 5, 6, 7, 9]))#2
print(Operations([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))#3
print(Music(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))#4
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(MainDiagonal(matrix))#5
print(Count(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))#6
print(Palindromes([121, 123, 12321, 44, 55, 678]))#7
print(ASCII(2, ["test", "hello", "lab002"], False))#8
stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
print(Stadium(stadium))#9
print(Lists([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"]))#10
print(Tuples([('abc', 'bcd'), ('abc', 'zza')]))#11
print(Rhymes(['ana', 'banana', 'carte', 'arme', 'parte']))#12