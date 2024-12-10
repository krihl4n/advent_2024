file_path = "input.txt"

area_map = []


def print_map():
    for r in area_map:
        for f in r:
            print(f, end="")
        print()
    print()


with open(file_path) as input_file:
    for line in input_file:
        row = list(line.strip("\n"))
        area_map.append(row)

start_x = 0
start_y = 0

for idx, row in enumerate(area_map):
    for idy, field in enumerate(row):
        if field == "^":
            start_x = idx
            start_y = idy

print_map()
print("start:", start_x, start_y)

is_finished = False
move_x = -1
move_y = 0

location_x = start_x
location_y = start_y

direction = [True, False, False, False] # up right down left

counter = 0

while not is_finished:
    # if counter % 500 == 0:
    #     #print_map()
    # counter += 1

    try:
        field = area_map[location_x][location_y]
    except IndexError:
        print_map()
        print(location_x, location_y)
        is_finished = True

    if field == "^" or field == ".":
        area_map[location_x][location_y] = "X"

    if field == "#":
        location_x = location_x + (-1*move_x)
        location_y = location_y + (-1*move_y)
        for i, current_direction in enumerate(direction):
            if current_direction:
                direction[i] = False
                next_index = i+1 if i + 1 < len(direction) else 0
                direction[next_index] = True
                break

        new_direction = direction.index(True)

        if new_direction == 0:
            move_x = -1
            move_y = 0
        elif new_direction == 1:
            move_x = 0
            move_y = 1
        elif new_direction == 2:
            move_x = 1
            move_y = 0
        elif new_direction == 3:
            move_x = 0
            move_y = -1

    location_x = location_x + move_x
    location_y = location_y + move_y
    print(location_x, location_y)
    if location_x >= len(area_map) or location_y >= len(area_map) or location_y < 0 or location_x < 0:
        is_finished = True


print_map()

sum = 0
for idx, row in enumerate(area_map):
    for idy, field in enumerate(row):
        if field == "X":
            sum += 1

print("sum:", sum)