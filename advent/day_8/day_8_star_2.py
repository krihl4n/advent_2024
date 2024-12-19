file_path = "input.txt"

points = [(3, 4), (5, 5)]

def find_antinodes_for(point_1, point_2, size):
    antinodes = []
    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]

    a = float((y1 - y2) / (x1 - x2))
    b = float(y1 - x1 * ((y1 - y2) / (x1 - x2)))

    print("a:", a)
    print("b:", b)

    step = abs(x1 - x2)

    if step > 0:
        starting_point = x1
        while starting_point - step >= 0:
            starting_point -= step

        x = starting_point
        while x < size:
            y = round(a * x + b)
            if 0 <= y < size:
                antinodes.append((x, y))
            x += step
    else:
        step = abs(y1 - y2)
        starting_point = y1
        while starting_point - step >= 0:
            starting_point -= step

        y = starting_point
        while y < size:
            x = (b - y) / a
            if 0 <= x < size:
                antinodes.append((x, int(y)))
            y += step

    return antinodes


# print(find_antinodes_for((4, 8),(5, 5), 10)) # expected (1, 3) (7, 6)
# print(find_antinodes_for((5, 6), (7, 11), 10))  # expected (1, 3) (7, 6)

antenna_map = []


def print_map():
    for r in antenna_map:
        for f in r:
            print(f, end="")
        print()
    print()


with open(file_path) as input_file:
    for line in input_file:
        row = list(line.strip("\n"))
        antenna_map.append(row)

print_map()

antennas_locations = dict()

for i, row in enumerate(antenna_map):
    for j, antenna in enumerate(row):
        if antenna != '.' and antenna != "#":
            if antenna in antennas_locations:
                l = antennas_locations[antenna]
                l.append((i, j))
                antennas_locations[antenna] = l
            else:
                antennas_locations[antenna] = [(i, j)]

# print(antennas_locations)
for k in antennas_locations.keys():
    print(k, antennas_locations[k])
unique_antinodes = []

for antenna in antennas_locations.keys():
    locations = antennas_locations[antenna]
    if len(locations) < 2:
        continue
    for idx, point1 in enumerate(locations):
        for point2 in locations[idx + 1:]:
            antinodes = find_antinodes_for(point1, point2, size=len(antenna_map))
            print("points:", point1, point2)
            print(antinodes)
            print()
            # if len(antinodes) == 2:
            #     continue
            for a in antinodes:
                if a not in unique_antinodes:
                    unique_antinodes.append(a)

unique_antinodes.sort()
print("unique antinodes: ", unique_antinodes)
print("result", len(unique_antinodes))

print(len(antenna_map))
print(len(antenna_map[1]))