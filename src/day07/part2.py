# input = [
#     '32T3K 765',
#     'T55J5 684',
#     'KK677 28',
#     'KTJJT 220',
#     'QQQJA 483',
# ]

with open('src/day07/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

cards = 'J23456789TQKA'

def card_value(card):
    return cards.index(card)

def hand_value(hand):
    freq = {card: hand.count(card) for card in set(hand)}
    
    play = 'high_card'
    
    if 5 in freq.values():
        play = 'five'
    elif 4 in freq.values():
        if freq.get('J') == 4 or freq.get('J') == 1:
            play = 'five'
        else:
            play = 'four'
    elif 3 in freq.values() and 2 in freq.values():
        if freq.get('J') == 3 or freq.get('J') == 2:
            play = 'five'
        elif freq.get('J') == 1:
            play = 'four'
        else:
            play = 'full'
    elif 3 in freq.values():
        if freq.get('J') == 3 or freq.get('J') == 1:
            play = 'four'
        else:
            play = 'three'
    elif list(freq.values()).count(2) == 2:
        if freq.get('J') == 2:
            play = 'four'
        elif freq.get('J') == 1:
            play = 'full'
        else:
            play = 'pairs'
    elif 2 in freq.values():
        if freq.get('J') == 2 or freq.get('J') == 1:
            play = 'three'
        else:
            play = 'pair'
    else: 
        if freq.get('J') == 1:
            play = 'pair'
        else:
            play = 'high_card'

    if play == 'five':
        return 60
    elif play == 'four':
        return 50
    elif play == 'full':
        return 40
    elif play == 'three':
        return 30
    elif play == 'pairs':
        return 20
    elif play == 'pair':
        return 10
    else:
        return 1
    
hands = []

for line in input:
    line_splited = line.split(' ')
    hands.append({
        'hand': line_splited[0],
        'bid': int(line_splited[1]),
        'value': hand_value(line_splited[0])
    })

sorted_hands = sorted(hands, key=lambda x: (x['value'], card_value(x['hand'][0]), card_value(x['hand'][1]), card_value(x['hand'][2]), card_value(x['hand'][3]), card_value(x['hand'][4])))

total = 0
for i in range(0, len(sorted_hands)):
    total += (i + 1) * sorted_hands[i]['bid']

print(total)
    