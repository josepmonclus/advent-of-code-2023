# input = [
#     'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#     'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#     'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#     'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#     'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#     'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
# ]

with open('src/day04/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

total_points = 0

for line in input:
    numbers = line.split(': ')[1]
    winning_numbers = numbers.split(' | ')[0].split(' ')
    own_numbers = numbers.split(' | ')[1].split(' ')
    #remove empty elements from arrays
    while ("" in winning_numbers):
        winning_numbers.remove("")
    while ("" in own_numbers):
        own_numbers.remove("")
        
    card_points = 0
    for n in own_numbers:
        if n in winning_numbers:
            if card_points == 0:
                card_points = 1
            else:
                card_points = card_points * 2
    
    total_points = total_points + card_points
print(total_points)