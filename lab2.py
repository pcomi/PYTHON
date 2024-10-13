#1
def base2(num):
    result = ""
    while num > 0:
        result += str(num % 2)
        num //= 2

    result += "b0"
    return result[::-1]

#2
def bin_hex(num):
    if num == 0:
        return "0x0"
    
    hex_chars = "0123456789ABCDEF"
    result = ""
    
    binary_string = ""
    while num > 0:
        binary_string = str(num % 2) + binary_string
        num //= 2
    
    while len(binary_string) % 4 != 0:
        binary_string = "0" + binary_string
    
    for i in range(0, len(binary_string), 4):
        nibble = binary_string[i:i + 4]
        hex_value = 0
        for bit in nibble:
            hex_value = hex_value * 2 + int(bit)
        result += hex_chars[hex_value]
    
    return "0x" + result

#3
def custombase(num, digits):
    result = ""

    while num > 0:
        result += digits[num%len(digits)]
        num //= len(digits)
    
    result += "x0"
    return result[::-1]

#4
def base16(num):
    digits = "0123456789ABCDEF"
    result = ""

    while num > 0:
        result += digits[num%16]
        num //= 16
    
    return result[::-1]

#5
def parantezare(str):
    counter = 0
    for i in range(len(str)):
        if str[i] == '(':
            counter += 1
        elif str[i] == ')':
            counter -= 1
    
    return counter == 0

#6
def asci(s):
    result = ""
    for i in range(len(s)):
        if(s[i] == ' '):
            result += '\n'
        else:
            result += base16(ord((s[i])))

    return result

#7
def uppercount(s):
    maj = 0
    for i in range(len(s)):
        if ord((s[i])) >= 65 and ord((s[i])) <= 90:
            maj += 1
    return maj

#8 - e grea

#9
def firstlast(s):
    a = s[0]
    for i in range(len(s)):
        if s[i] == ' ':
            print(a, s[i-1])
            a = s[i+1]
    
    print(a, s[len(s) - 1])

#10
def rev(s):
    result = ""
    index = len(s) - 1
    index2 = len(s)

    while index > 0:
        if s[index] == ' ':
            for i in range(index + 1, index2):
                result += s[i]
            result += ' '
            index2 = index
        index -= 1

    for i in range(len(s)):
        result += s[i]
        if s[i+1] == ' ':
            break

    return result

#11
def consvoc(s):
    cons = 0
    vocs = 0
    vowels = "aeiouAEIOU"

    for i in range(len(s)):
        if s[i] in vowels:
            vocs += 1
        elif s[i] != ' ':
            cons += 1
    
    print(f"vocale: {vocs}\nconsoane: {cons}")

#12
def palindrome(num):
    rnum = 0
    temp = 1
    aux = num

    while aux > 9:
        aux //= 10
        temp *= 10
    
    aux = num
    while aux:
        rnum += (aux % 10) * temp
        aux //= 10
        temp //= 10

    if rnum == num:
        return True
    else:
        return False

print(base2(10))#1
print(bin_hex(22))#2
print(custombase(301, "abcd"))#3
print(base16(1234))#4
print(parantezare("8-4*(3+7/8+4/(5-9)"))#5
print(asci("abc 012"))#6
print(uppercount("A fost, de asemenea, Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele-state Grecesti."))#7
firstlast("ana are mere multe")#9
print(rev("ana are mere multe"))#10
consvoc("ana are mere multe")#11
print(palindrome(1221))#12