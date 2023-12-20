# input = [
#     '32T3K 765',
#     'T55J5 684',
#     'KK677 28',
#     'KTJJT 220',
#     'QQQJA 483',
# ]

with open('src/day07/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

cards = '23456789TJQKA'

def card_value(card):
    return cards.index(card)

def hand_value(hand):
    freq = {card: hand.count(card) for card in set(hand)}
    
    if 5 in freq.values():
        # 5 of a kind
        return 60
    if 4 in freq.values():
        # 4 of a kind
        return 50
    if 3 in freq.values() and 2 in freq.values():
        # full house
        return 40
    if 3 in freq.values():
        # 3 of a kind
        return 30
    if list(freq.values()).count(2) == 2:
        # two pair
        return 20
    if 2 in freq.values():
        # pair
        return 10
    else: 
        return 1
    
hands = []

for line in input:
    line_splited = line.split(' ')
    hands.append({
        'hand': line_splited[0],
        'bid': int(line_splited[1]),
        'hand_ordered': "".join(sorted(line_splited[0], key=card_value)),
        'value': hand_value(line_splited[0])
    })

sorted_hands = sorted(hands, key=lambda x: (x['value'], card_value(x['hand'][0]), card_value(x['hand'][1]), card_value(x['hand'][2]), card_value(x['hand'][3]), card_value(x['hand'][4])))

total = 0
for i in range(0, len(sorted_hands)):
    total += (i + 1) * sorted_hands[i]['bid']

print(total)
    