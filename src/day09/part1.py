def all_zeros(array: []) -> bool:
    for item in array:
        if item != 0:
            return False
    return True
    
input = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45',
]

with open('src/day09/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

extrapolated_values = []

work = []
for line in input:
    work = []
    
    work.append(list(map(int, line.split())))
    
    i = 0
    while not all_zeros(work[i]):
        _w = []
        for j in range(1, len(work[i])):
            _w.append(work[i][j] - work[i][j - 1])
        work.append(_w)
        i += 1
    
    for i in range(len(work) - 1, -1, -1):
        if i == len(work) - 1:
            _w = 0
        else:
            _w = _w + work[i][-1]
        
        work[i].append(_w)
        
        if i == 0:
            extrapolated_values.append(_w)

print(sum(extrapolated_values))