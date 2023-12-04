# input = [
#     '1abc2',
#     'pqr3stu8vwx',
#     'a1b2c3d4e5f',
#     'treb7uchet',
# ]

with open('src/day01/input.txt', "r") as archivo:
    input = archivo.readlines()

total = 0

for line in input:
    first = 0
    last = 0
    for letter in line:
        if(letter.isdigit()):
            if first == 0:
                first = int(letter)
            last = int(letter)
    n = first * 10 + last
    total = total + n

print(total)