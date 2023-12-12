def find_equivalent(conversions, item_to_find):
    item_converted = item_to_find
    
    for conversion in conversions:
        if item_to_find >= conversion[0] and item_to_find < conversion[0] + conversion[2]:
            item_converted = conversion[1] + (item_to_find - conversion[0])
            break

    return item_converted
    
def find_seed(location):
    humidity = find_equivalent(humidity_to_location, location)
    temperature = find_equivalent(temperature_to_humidity, humidity)
    light = find_equivalent(light_to_temperature, temperature)
    water = find_equivalent(water_to_light, light)
    fertilizer = find_equivalent(fertilizer_to_water, water)
    soil = find_equivalent(soil_to_fertilizer, fertilizer)
    seed = find_equivalent(seed_to_soil, soil)
    
    # print(f'{seed} -> {soil} -> {fertilizer} -> {water} -> {light} -> {temperature} -> {humidity} -> {location}')

    return seed

# with open('src/day05/test.txt', "r") as file:
#     input = [line.strip() for line in file.readlines()]

with open('src/day05/input.txt', "r") as file:
    input = [line.strip() for line in file.readlines()]

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

min_location = -1

# parse almanac
for i in range(0, len(input)):
    line = input[i]
    
    if line.startswith('seeds'):
        seeds = line.split(': ')[1].split(' ')
    elif line.startswith('seed-to-soil'):
        i += 1
        line = input[i]
        while line != '':
            seed_to_soil.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('soil-to-fertilizer'):
        i += 1
        line = input[i]
        while line != '':
            soil_to_fertilizer.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('fertilizer-to-water'):
        i += 1
        line = input[i]
        while line != '':
            fertilizer_to_water.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('water-to-light'):
        i += 1
        line = input[i]
        while line != '':
            water_to_light.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('light-to-temperature'):
        i += 1
        line = input[i]
        while line != '':
            light_to_temperature.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('temperature-to-humidity'):
        i += 1
        line = input[i]
        while line != '':
            temperature_to_humidity.append(line.split(' '))
            i += 1
            line = input[i]
    elif line.startswith('humidity-to-location'):
        i += 1
        line = input[i]
        while line != '':
            humidity_to_location.append(line.split(' '))
            i += 1
            line = input[i] if i < len(input) else ''
            
seeds = list(map(int, seeds))
seed_to_soil = [list(map(int, subarray))  for subarray in seed_to_soil]
soil_to_fertilizer = [list(map(int, subarray))  for subarray in soil_to_fertilizer]
fertilizer_to_water = [list(map(int, subarray))  for subarray in fertilizer_to_water]
water_to_light = [list(map(int, subarray))  for subarray in water_to_light]
light_to_temperature = [list(map(int, subarray))  for subarray in light_to_temperature]
temperature_to_humidity = [list(map(int, subarray))  for subarray in temperature_to_humidity]
humidity_to_location = [list(map(int, subarray))  for subarray in humidity_to_location]

found = False
while not found:
    min_location += 1
    seed = find_seed(min_location)
    
    for pair in range(0, len(seeds) // 2):
        if seed >= seeds[pair * 2] and seed < seeds[pair * 2] + seeds[pair * 2 + 1]:
            found = True
            break
    
print(min_location)

