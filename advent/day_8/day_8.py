file_path = "input.txt"

points = [(3, 4), (5, 5)]

def find_antinodes_for(point_1, point_2, size):
    dist_x = abs(point_1[0] - point_2[0])
    dist_y = abs(point_1[1] - point_2[1])

    res_x1 = point_1[0]
    res_x2 = point_1[0]
    if point_1[0] < point_2[0]:
        res_x1 = point_1[0] - dist_x
        res_x2 = point_2[0] + dist_x
    elif point_1[0] > point_2[0]:
        res_x1 = point_2[0] - dist_x
        res_x2 = point_1[0] + dist_x

    res_y1 = point_1[1]
    res_y2 = point_1[1]

    if point_1[1] < point_2[1]:
        res_y1 = point_1[1] - dist_y
        res_y2 = point_2[1] + dist_y
    elif point_1[1] > point_2[1]:
        res_y1 = point_2[1] - dist_y
        res_y2 = point_1[1] + dist_y

    antinodes = []

    if point_1[0] < point_2[0] and point_1[1] > point_2[1]:
        a1 = (res_x1, res_y2)
        a2 = (res_x2, res_y1)
    else:
        a1 = (res_x1, res_y1)
        a2 = (res_x2, res_y2)

    if a1[0] < size and a1[1] < size and a1[0] >= 0 and a1[1] >= 0:
        antinodes.append(a1)

    if a2[0] < size and a2[1] < size and a2[0] >= 0 and a2[1] >= 0:
        antinodes.append(a2)

    print("antinodes for {}{} are {}".format( point_1, point_2, antinodes))
    return antinodes

#print(find_antinodes_for((4, 8),(5, 5), 10)) # expected (1, 3) (7, 6)

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

print(antennas_locations)

unique_antinodes = []

for antenna in antennas_locations.keys():
    locations = antennas_locations[antenna]

    for idx, point1 in  enumerate(locations):
        for point2 in locations[idx+1:]:
            antinodes = find_antinodes_for(point1, point2, size = len(antenna_map))
            print(antinodes)
            for a in antinodes:
                if a not in unique_antinodes:
                    unique_antinodes.append(a)

print("unique antinodes: ", unique_antinodes)
print("result", len(unique_antinodes))