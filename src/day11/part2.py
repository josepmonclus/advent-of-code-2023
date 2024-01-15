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
expand_factor = 1000000

# EXPAND UNIVERSE
# Expand rows
rows_to_expand = []
for i, row in enumerate(input):
    expaded_universe.append(row)
    if '#' not in row:
        rows_to_expand.append(i)

#Expand columns
cols_to_expand = []
for j in range(len(input[0]) - 1, -1, -1):
    galaxies = False
    for i, row in enumerate(input):
        if row[j] != '.':
            galaxies = True
            break
    
    if not galaxies:
        cols_to_expand.append(j)

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
        
        for row_to_expand in rows_to_expand:
            row_range = range(position_a[0], position_b[0]) if position_a[0] <= position_b[0] else range(position_b[0], position_a[0])
            if row_to_expand in row_range:
                steps -= 1
                steps += expand_factor
        
        for col_to_expand in cols_to_expand:
            col_range = range(position_a[1], position_b[1]) if position_a[1] <= position_b[1] else range(position_b[1], position_a[1])
            if col_to_expand in col_range:
                steps -= 1
                steps += expand_factor
        
        sum_shortest_paths += steps


print(sum_shortest_paths)