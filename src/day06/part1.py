# input = [
#     'Time:      7  15   30',
#     'Distance:  9  40  200',
# ]

with open('src/day06/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

# Parse times
times = input[0].split(':')[1].strip().split(' ')
while ("" in times):
        times.remove("")
times = list(map(int, times))

# Parse distances
distances = input[1].split(':')[1].strip().split(' ')
while ("" in distances):
        distances.remove("")
distances = list(map(int, distances))

result = 1

for race in range(0, len(times)):
    wins = 0
    for i in range(1, times[race] + 1):
        hold = i
        run = times[race] - hold
        
        if run * hold > distances[race]:
            wins += 1
    
    result = result * wins

print(result)