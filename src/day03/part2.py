input = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
    '*12...*123'
]

for row in range(0, len(input)):
    line = input[row]
    # print(line)
    for col in range(0, len(line)):
        if line[col] == '*':
            left = ''
            if col > 0 and line[col - 1].isdigit():
                k = 1
                while True:
                    if col - k < 0 or not line[col - k].isdigit():
                        break
                    else:
                        left = line[col - k] + left
                        k = k + 1
            
            right = ''
            if col < len(line) - 1 and line[col + 1].isdigit():
                k = 1
                while True:
                    if col + k == len(line) or not line[col + k].isdigit():
                        break
                    else:
                        right = right + line[col + k]
                        k = k + 1
            
            start_with_diag = col - 1 if col > 0 else 0
            end_with_diag = start_with_diag + 2 if col > 0 and col < len(line) - 1 else start_with_diag + 1
            
            top = ''
            if row > 0:
                top = input[row - 1][start_with_diag:end_with_diag + 1]
            
            bot = ''
            if row < len(input) - 1:
                bot = input[row + 1][start_with_diag:end_with_diag + 1]
            
            print(f'{left} - {right} - {top} - {bot}')
            