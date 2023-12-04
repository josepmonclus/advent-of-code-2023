# input = [
#     'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
# ]

with open('data/day02.txt', "r") as archivo:
    input = archivo.readlines()
    
sum_powers = 0

for game in input:
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    
    id = game.split(':')[0].split(' ')[1]
    sets = game.split(':')[1].split(';')
    sets = list(map(lambda set: set.strip(), sets))
    
    for s in sets:
        for cubes in s.split(','):
            n = int(cubes.strip().split(' ')[0])
            color = cubes.strip().split(' ')[1]
            
            if min_cubes[color] < n:
                min_cubes[color] = n
            
    power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']    
    sum_powers = sum_powers + power

print(sum_powers)
