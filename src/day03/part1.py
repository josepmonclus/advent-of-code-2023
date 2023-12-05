# input = [
#     '467..114..',
#     '...*......',
#     '..35...633',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..',
# ]

with open('src/day03/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

total_sum = 0
no_part_nums = []
part_nums = []

for row in range(0, len(input)):
    line = input[row]
    n = ''
    for col in range(0, len(line)):
        char = line[col]
        if char.isdigit():
            n = n + char
        
        if n.isdigit() and (col == len(line) - 1 or not line[col + 1].isdigit()):
            start = col - len(n) + 1
            end = col
            
            left = '.'
            right = '.'
            top = '.'
            bot = '.'
            
            # left side
            if start > 0 and line[start - 1] != '.' and not line[start - 1].isdigit():
                left = line[start - 1]
            #right side
            if end < len(line) - 1 and line[end + 1] != '.' and not line[end + 1].isdigit():
                right = line[end + 1]
                
            start_with_diag = start - 1 if start > 0 else 0
            end_with_diag = end + 1 if end < len(line) else end
            
            #top with diagonals
            if row > 0:
                top = input[row - 1][start_with_diag:end_with_diag + 1]
            
            #bot with diagonals
            if row < len(input) - 1:
                bot = input[row + 1][start_with_diag:end_with_diag + 1]
            
            if(
                left != '.' or
                right != '.' or
                any((c != '.' and not c.isdigit()) for c in top) or
                any((c != '.' and not c.isdigit()) for c in bot)
            ):
                part_nums.append(int(n))
            
            n = ''

print(sum(part_nums))