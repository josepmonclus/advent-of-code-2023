input = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]

with open('src/day11/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

sum_shortest_paths = 0

expaded_universe = []

# EXPAND UNIVERSE
# Expand rows
for i, row in enumerate(input):
    expaded_universe.append(row)
    if '#' not in row:
        expaded_universe.append(row)

#Expand columns
for j in range(len(input[0]) - 1, -1, -1):
    galaxies = False
    for i, row in enumerate(input):
        if row[j] != '.':
            galaxies = True
            break
    
    if not galaxies:
        # have to expand!
        for i, row in enumerate(expaded_universe):
            expaded_universe[i] = row[:j+1] + '.' + row[j+1:]
            
# Assign numbers to galaxies and save positions
galaxy_n = 0
galaxies_positions = {}
for i, row in enumerate(expaded_universe):
    for j, item in enumerate(row):
        if item == '#':
            galaxy_n += 1
            expaded_universe[i] = expaded_universe[i][:j] + str(galaxy_n) + expaded_universe[i][j+1:]
            galaxies_positions[galaxy_n] = [i, j]

# find pairs
for a in range(1, galaxy_n + 1):
    for b in range(a + 1, galaxy_n + 1):
        position_a = galaxies_positions[a]
        position_b = galaxies_positions[b]
        steps = abs(position_a[0] - position_b[0]) + abs(position_a[1] - position_b[1])
        sum_shortest_paths += steps

print(sum_shortest_paths)