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

locations = []

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

for seed in seeds:
    # find soil
    soil = seed
    for e in seed_to_soil:
        if seed >= e[1] and seed < e[1] + e[2]:
            diff = seed - e[1]
            soil = e[0] + diff
            break
    # find fertilizer
    fertilizer = soil
    for e in soil_to_fertilizer:
        if soil >= e[1] and soil < e[1] + e[2]:
            diff = soil - e[1]
            fertilizer = e[0] + diff
            break
    # find water
    water = fertilizer
    for e in fertilizer_to_water:
        if fertilizer >= e[1] and fertilizer < e[1] + e[2]:
            diff = fertilizer - e[1]
            water = e[0] + diff
            break
    # find light
    light = water
    for e in water_to_light:
        if water >= e[1] and water < e[1] + e[2]:
            diff = water - e[1]
            light = e[0] + diff
            break
    # find temperature
    temperature = light
    for e in light_to_temperature:
        if light >= e[1] and light < e[1] + e[2]:
            diff = light - e[1]
            temperature = e[0] + diff
            break
    # find humidity
    humidity = temperature
    for e in temperature_to_humidity:
        if temperature >= e[1] and temperature < e[1] + e[2]:
            diff = temperature - e[1]
            humidity = e[0] + diff
            break
    # find location
    location = humidity
    for e in humidity_to_location:
        if humidity >= e[1] and humidity < e[1] + e[2]:
            diff = humidity - e[1]
            location = e[0] + diff
            break
    locations.append(location)
            
    # print(f'{seed} -> {soil} -> {fertilizer} -> {water} -> {light} -> {temperature} -> {humidity} -> {location}')

print(min(locations))