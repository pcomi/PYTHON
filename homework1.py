#1
def cmmdc(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1

#2
def vowels(str):
    vowels = "aeiouAEIOU"
    counter = 0

    for i in range(len(str)):
        if str[i] in vowels:
            counter += 1

    return counter

#3
def substrings(str1, str2):
    return str1.count(str2)

#4
def lowerstring(str):
    aux = ""
    for i in range(len(str)):
        if str[i].isupper() and aux == "":
            aux += str[i].lower()
        elif str[i].isupper():
            aux += "_"
            aux += str[i].lower()
        else:
            aux += str[i]
    return aux

#5
def palindrome(n):
    strn = str(n)
    for i in range(int(len(strn) / 2)):
        if strn[i] != strn[len(strn) - i - 1]:
            return False
    return True

#6
def findnumber(str):
    numbers = "1234567890"
    number = ""

    for i in range(len(str)):
        if str[i] in numbers:
            number += str[i]
            i += 1
            while str[i] in numbers:
                number += str[i]
                i += 1
        if number != "":
            return number
        
#7
def bits(n):
    counter = 0

    while n != 0:
        if n%2 == 1:
            counter += 1
        n = int(n / 2)
    
    return counter

#8
def words(str):
    counter = 1

    for i in range(len(str)):
        if str[i] == " ":
            counter += 1
    
    return counter

#number1 = int(input("Enter first number: "))
#number2 = int(input("Enter second number: "))

#print(cmmdc(number1, number2))

#print(vowels("Ana are mere"))

#print(substrings("anaaremereanasianaana","ana"))

#print(lowerstring("UpperCamelCase"))

#print(palindrome(1221))

#print(findnumber("abc123abc"))

#print(bits(24))

#print(words("I have Python exam" ))