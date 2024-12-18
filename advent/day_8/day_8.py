file_path = "test_input.txt"

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

    if res_x1 < size and res_y1 < size:
        antinodes.append((res_x1, res_y1))

    if res_x2 < size and res_y2 < size:
        antinodes.append((res_x2, res_y2))

    print("antinodes for {}{} are {}".format( point_1, point_2, antinodes))
    return antinodes

print(find_antinodes_for((4, 8),(5, 5), 10)) # expected (1, 3) (7, 6)

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

for antenna in antennas_locations.keys():
    locations = antennas_locations[antenna]

    for idx, point1 in  enumerate(locations):
        for point2 in locations[idx+1:]:
            antinodes = find_antinodes_for(point1, point2, size = len(antenna_map))
            print(antinodes)

