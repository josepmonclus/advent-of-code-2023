# input = [
#     'two1nine',
#     'eightwothree',
#     'abcone2threexyz',
#     'xtwone3four',
#     '4nineeightseven2',
#     'zoneight234',
#     '7pqrstsixteen',
# ]

with open('src/day01/input.txt', "r") as archivo:
    input = archivo.readlines()

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

total = 0

for line in input:
    first = 0
    last = 0
    for i in range(0, len(line)):
        letter = line[i]
        if(letter.isdigit()):
            if first == 0:
                first = int(letter)
            last = int(letter)
        else:
            for number in numbers:
                if len(number) <= len(line) - i:
                    if number == line[i:i+len(number)]:
                        if first == 0:
                            first = numbers[number]
                        last = numbers[number]
    n = first * 10 + last
    total = total + n

print(total)