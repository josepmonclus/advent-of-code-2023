# input = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
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
    
sum_prods = 0

for row in range(0, len(input)):
    line = input[row]
    # print(line)
    for col in range(0, len(line)):
        if line[col] == '*':
            gear_parts = []
            left = ''
            if col > 0 and line[col - 1].isdigit():
                k = 1
                while True:
                    if col - k < 0 or not line[col - k].isdigit():
                        break
                    else:
                        left = line[col - k] + left
                        k = k + 1
            if left != '':
                gear_parts.append(left)
            
            right = ''
            if col < len(line) - 1 and line[col + 1].isdigit():
                k = 1
                while True:
                    if col + k == len(line) or not line[col + k].isdigit():
                        break
                    else:
                        right = right + line[col + k]
                        k = k + 1
            if right != '':
                gear_parts.append(right)
            
            start_with_diag = col - 1 if col > 0 else 0
            end_with_diag = start_with_diag + 2 if col > 0 and col < len(line) - 1 else start_with_diag + 1
            
            top = ''
            if row > 0:
                aux = input[row - 1][start_with_diag:end_with_diag + 1]
                for i in range(0, len(aux)):
                    if aux[i].isdigit():
                        if i == 0:
                            k = 1
                            while True:
                                if start_with_diag - k < 0 or not input[row - 1][start_with_diag - k].isdigit():
                                    break
                                else:
                                    top = input[row - 1][start_with_diag - k] + top
                                    k = k + 1
                        top = top + input[row - 1][start_with_diag + i]
                        
                        if i == len(aux) - 1 and input[row - 1][start_with_diag + i + 1].isdigit():
                            k = 1
                            while True:
                                if start_with_diag + i + k == len(input[row - 1]) or not input[row - 1][start_with_diag + i + k].isdigit():
                                    break
                                else:
                                    top = top + input[row - 1][start_with_diag + i + k]
                                    k = k + 1
                    else:
                        if top != '':
                            gear_parts.append(top)
                            top = ''
            if top != '':
                gear_parts.append(top)
                
            bot = ''
            if row < len(input) - 1:
                aux = input[row + 1][start_with_diag:end_with_diag + 1]
                for i in range(0, len(aux)):
                    if aux[i].isdigit():
                        if i == 0:
                            k = 1
                            while True:
                                if start_with_diag - k < 0 or not input[row + 1][start_with_diag - k].isdigit():
                                    break
                                else:
                                    bot = input[row + 1][start_with_diag - k] + bot
                                    k = k + 1
                        bot = bot + input[row + 1][start_with_diag + i]
                        
                        if i == len(aux) - 1 and input[row + 1][start_with_diag + i + 1].isdigit():
                            k = 1
                            while True:
                                if start_with_diag + i + k == len(input[row + 1]) or not input[row + 1][start_with_diag + i + k].isdigit():
                                    break
                                else:
                                    bot = bot + input[row + 1][start_with_diag + i + k]
                                    k = k + 1
                    else:
                        if bot != '':
                            gear_parts.append(bot)
                            bot = ''
            if bot != '':
                gear_parts.append(bot)
            
            if len(gear_parts) > 1:
                prod = 0
                for part in gear_parts:
                    prod = (prod if prod > 0 else 1) * int(part)
                sum_prods = sum_prods + prod

print(sum_prods)