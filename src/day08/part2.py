def validate_actual_place(actual_place):
    for place in actual_place:
        if not place.endswith('Z'):
            return False
    return True
    
input = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]

with open('src/day08/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

instructions = input[0]
paths = {}

for i in range(2, len(input)):
    paths[input[i].split(' = ')[0]] = (
        input[i].split(' = ')[1].split(', ')[0][1::],
        input[i].split(' = ')[1].split(', ')[1][:3]
    )
# print(paths)
steps = 0

actual_place = [key for key in paths.keys() if key.endswith('A')]
# print(actual_place)
while not validate_actual_place(actual_place):
    for instruction in instructions:
        _new_places = []
        for place in actual_place:
            if instruction == 'L':
                _new_places.append(paths[place][0])
            else:
                _new_places.append(paths[place][1])
        
        actual_place = _new_places
        steps += 1
        
        # print(f'{actual_place} - {steps}')
        
        if validate_actual_place(actual_place):
            break

print(steps)