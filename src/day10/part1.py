'''
L - pipe connect N and E
J - pipe connect N and W
F - pipe connect S and E
7 - pipe connect S and W
- - horizontal pipe
| - vertical pipe
'''

input = [
    '.....',
    '.S-7.',
    '.|.|.',
    '.L-J.',
    '.....',
]

input = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...',
]

with open('src/day10/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

initial_position = []

for i, line in enumerate(input):
    for j, item in enumerate(line):
        if item == 'S':
            initial_position = [i, j]
            
print(initial_position)

steps = 0
actual_position = initial_position
previous_position = []
to = ''

if actual_position[0] > 0 and input[actual_position[0] - 1][actual_position[1]] != '.' and input[actual_position[0] - 1][actual_position[1]] in ['|', '7', 'F']:
    #to => NORTH
    previous_position = 'SOUTH'
    actual_position = [actual_position[0] - 1, actual_position[1]]
elif actual_position[1] < len(input[actual_position[0]]) - 1 and input[actual_position[0]][actual_position[1] + 1] != '.' and input[actual_position[0]][actual_position[1] + 1] in ['-', '7', 'J']:
    # to => EAST
    previous_position = 'WEST'
    actual_position = [actual_position[0], actual_position[1] + 1]
elif actual_position[0] < len(input) - 1 and input[actual_position[0] + 1][actual_position[1]] != '.' and input[actual_position[0] + 1][actual_position[1]] in ['|', 'J', 'L']:
    #to => SOUTH
    previous_position = 'NORTH'
    actual_position = [actual_position[0] + 1, actual_position[1]]
elif actual_position[1] > 0 and input[actual_position[0]][actual_position[1] + 1] != '.' and input[actual_position[0]][actual_position[1] + 1] in ['-', 'L', 'F']:
    # to => WEST
    previous_position = 'EAST'
    actual_position = [actual_position[0], actual_position[1] - 1]

steps += 1
    
while input[actual_position[0]][actual_position[1]] != 'S':
    print(f'{actual_position} from {previous_position} -> {input[actual_position[0]][actual_position[1]]}')
    if input[actual_position[0]][actual_position[1]] == '|':
        if previous_position == 'NORTH':
            # to => SOUTH
            actual_position = [actual_position[0] + 1, actual_position[1]]
        else:
            # to => NORTH
            actual_position = [actual_position[0] - 1, actual_position[1]]
    elif input[actual_position[0]][actual_position[1]] == '-':
        if previous_position == 'WEST':
            actual_position = [actual_position[0], actual_position[1] + 1]
        else: 
            actual_position = [actual_position[0], actual_position[1] - 1]
    elif input[actual_position[0]][actual_position[1]] == 'L':
        if previous_position == 'NORTH':
            actual_position = [actual_position[0], actual_position[1] + 1]
            previous_position = 'WEST'
        else:
            actual_position = [actual_position[0] - 1, actual_position[1]]
            previous_position = 'SOUTH'
    elif input[actual_position[0]][actual_position[1]] == 'J':
        if previous_position == 'NORTH':
            actual_position = [actual_position[0], actual_position[1] - 1]
            previous_position = 'EAST'
        else:
            actual_position = [actual_position[0] - 1, actual_position[1]]
            previous_position = 'SOUTH'
    elif input[actual_position[0]][actual_position[1]] == 'F':
        if previous_position == 'SOUTH':
            actual_position = [actual_position[0], actual_position[1] + 1]
            previous_position = 'WEST'
        else:
            actual_position = [actual_position[0] + 1, actual_position[1]]
            previous_position = 'NORTH'
    elif input[actual_position[0]][actual_position[1]] == '7':
        if previous_position == 'SOUTH':
            actual_position = [actual_position[0], actual_position[1] - 1]
            previous_position = 'EAST'
        else:
            actual_position = [actual_position[0] + 1, actual_position[1]]
            previous_position = 'NORTH'
    else:
        print('ERROR!')
        break
    
    steps += 1

print(f'{steps} total steps, animal is {steps // 2} steps away!')