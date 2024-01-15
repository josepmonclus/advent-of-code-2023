# input = [
#     'RL',
#     '',
#     'AAA = (BBB, CCC)',
#     'BBB = (DDD, EEE)',
#     'CCC = (ZZZ, GGG)',
#     'DDD = (DDD, DDD)',
#     'EEE = (EEE, EEE)',
#     'GGG = (GGG, GGG)',
#     'ZZZ = (ZZZ, ZZZ)',
# ]

# input = [
#     'LLR',
#     '',
#     'AAA = (BBB, BBB)',
#     'BBB = (AAA, ZZZ)',
#     'ZZZ = (ZZZ, ZZZ)',
# ]

with open('src/day08/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

instructions = input[0]
paths = {}

for i in range(2, len(input)):
    paths[input[i].split(' = ')[0]] = (
        input[i].split(' = ')[1].split(', ')[0][1::],
        input[i].split(' = ')[1].split(', ')[1][:3]
    )

actual_place = 'AAA'
steps = 0
while actual_place != 'ZZZ':
    for instruction in instructions:
        if instruction == 'L':
            actual_place = paths[actual_place][0]
        elif instruction == 'R':
            actual_place = paths[actual_place][1]
        
        steps += 1
        
        if actual_place == 'ZZZ':
            break
        
print(steps)