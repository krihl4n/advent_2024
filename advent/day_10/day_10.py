path = 'input.txt'

print()

input = []

def to_ints(array):
    result = []
    for el in array:
        row = []
        for el1 in el:
            if el1 == '.':
                row.append(-9)
            else:
                row.append(int(el1))
        result.append(row)
    return result


with open(path) as file:
    for x, line in enumerate(file):
        input.append(list(line.strip("\n")))

for el in input:
    print(el)

input = to_ints(input)

trailheads = []
peaks = []

for x, row in enumerate(input):
    for y, el in enumerate(row):
        if el == 0:
            trailheads.append((x, y))
        if el == 9:
            peaks.append((x, y))

print("trailheads:", trailheads)
print("peaks:", peaks)


# trailhead = trailheads[0]
# peak = peaks[0]
#
# location = trailhead

def next_location_valid(current_location, next_location):
    if next_location[0] < 0 or next_location[1] < 0 or next_location[0] >= len(input) or next_location[1] >= len(input):
        return False

    current_height = input[current_location[0]][current_location[1]]
    next_height = input[next_location[0]][next_location[1]]

    diff = next_height - current_height
    return diff == 0 or diff == 1

possible_locations = dict()

for x, row in enumerate(input):
    for y, loc in enumerate(row):
        if loc == -9:
            continue
        next_possible_locations = []

        if next_location_valid((x, y), (x, y-1)):
            next_possible_locations.append((x, y-1))

        if next_location_valid((x, y), (x, y+1)):
            next_possible_locations.append((x, y+1))

        if next_location_valid((x, y), (x-1, y)):
            next_possible_locations.append((x-1, y))

        if next_location_valid((x, y), (x+1, y)):
            next_possible_locations.append((x+1, y))

        possible_locations[(x, y)] = next_possible_locations

# for pl in possible_locations:
#     print(pl, possible_locations[pl])


counter = 0

for th in trailheads:
    start = th
    print("start:", start)
    locations_to_try = possible_locations[start]
    peaks_reached = []

    while len(locations_to_try) > 0:
        next_loc = locations_to_try.pop()
        if input[next_loc[0]][next_loc[1]] == 9:
            peaks_reached.append(next_loc)
        locations_to_try += possible_locations[next_loc]
        if next_loc in locations_to_try:
            locations_to_try.remove(next_loc) #??? keep track of trails?
    counter += len(peaks_reached)

    print("peaks reached:", peaks_reached)
print("number:", counter)
