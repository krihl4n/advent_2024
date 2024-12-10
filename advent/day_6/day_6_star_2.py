file_path = "test_input.txt"

# does not work, it's not just rectangles!

area_map = []

def print_map():
    for r in area_map:
        for f in r:
            print(f, " ",  end="")
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

last_3_corners = []
while not is_finished:

    field = area_map[location_x][location_y]
    if field == "^" or field == ".":
        area_map[location_x][location_y] = "X"

    if field == "#":
        location_x = location_x + (-1*move_x)
        location_y = location_y + (-1*move_y)

        if len(last_3_corners) > 2:
            last_3_corners.pop(0)
        last_3_corners.append((location_x, location_y))

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

    if location_x >= len(area_map) or location_y >= len(area_map) or location_y < 0 or location_x < 0:
        is_finished = True

    if len(last_3_corners) == 3 and abs(last_3_corners[0][0] - last_3_corners[2][0]) == abs(last_3_corners[1][0] - location_x) and abs(last_3_corners[0][1] - last_3_corners[2][1]) == abs(last_3_corners[1][1] - location_y): # is rectangle?
        a_x = last_3_corners[0][0]
        a_y = last_3_corners[0][1]
        b_x = location_x
        b_y = location_y

        open_path = True
        if a_x == b_x:
            if a_y > b_y:
                for y in range(b_y, a_y):
                    if area_map[a_x][y] == "#":
                        open_path = False
            else:
                for y in range(a_y, b_y):
                    if area_map[a_x][y] == "#":
                        open_path = False

        if a_y == b_y:
            if a_x > b_x:
                for x in range(b_x, a_x):
                    if area_map[x][a_y] == "#":
                        open_path = False
            else:
                for x in range(a_x, b_x):
                    if area_map[x][a_y] == "#":
                        open_path = False

        if open_path:
            possible_obstacle_x = location_x + move_x
            possible_obstacle_y = location_y + move_y
            if area_map[possible_obstacle_x][possible_obstacle_y] != "#":
                print("obstacle!", possible_obstacle_x, possible_obstacle_y)
                #is_finished = True


print_map()

sum = 0
for idx, row in enumerate(area_map):
    for idy, field in enumerate(row):
        if field == "X":
            sum += 1

print("sum:", sum)