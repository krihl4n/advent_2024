file_path = "test_input.txt"

points = [(3, 4), (5, 5)]

def find_antinodes_for(point_1, point_2, size):


    antinodes = []

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