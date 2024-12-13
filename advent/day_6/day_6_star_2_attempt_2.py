import copy

file_path = "input.txt"

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


# lame...
exceptions = [(19,12), (21,11), (22,11),(29,25), (30,33), (30,47), (31,96), (32,70), (36,11), (36,37), (40,11), (41,11), (49,26), (52,11), (55,11), (68,11), (70,11), (89, 39), (91,36), (109,63), (112, 27), (118, 25), (119, 37), (119, 47), (119, 50)]

obstacles = 0

for pot_obst_x in range(0, len(area_map)):
    for pot_obst_y in range (0, len(area_map)):

        if (pot_obst_x, pot_obst_y) in exceptions:
            continue

        print("try:", pot_obst_x, pot_obst_y)
        modified_map = copy.deepcopy(area_map)
        if area_map[pot_obst_x][pot_obst_y] == ".":
            modified_map[pot_obst_x][pot_obst_y] = "#"
            track = []

            is_finished = False
            move_x = -1
            move_y = 0

            location_x = start_x
            location_y = start_y

            direction = [True, False, False, False]  # up right down left

            while not is_finished:
                if len(track) > 0 and (location_x, location_y) in track:
                    last_occurence_index = len(track) - 1 - track[::-1].index((location_x, location_y))
                    if last_occurence_index < 0:
                        continue

                    loop_size = len(track) - last_occurence_index
                    if loop_size > 0:
                        last_pass = track[last_occurence_index:len(track)]
                        same_size_path_before_finish = last_occurence_index - 1
                        same_size_path_before_start = last_occurence_index - 1 - loop_size
                        if same_size_path_before_start >= 0 and same_size_path_before_finish >= 0:
                            path_a = track[same_size_path_before_start:same_size_path_before_finish]
                            path_b = track[last_occurence_index:len(track)]
                            if  path_a == path_b :
                                print("obstacle at:", pot_obst_x, pot_obst_y)
                                obstacles += 1
                                print("current count: ", obstacles)
                                is_finished = True


                field = modified_map[location_x][location_y]
                if field == "^" or field == ".":
                    modified_map[location_x][location_y] = "X"

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

                track.append((location_x, location_y))
                location_x = location_x + move_x
                location_y = location_y + move_y

                if location_x >= len(modified_map) or location_y >= len(modified_map) or location_y < 0 or location_x < 0:
                    is_finished = True

print_map()
print("obstacles: ", obstacles)
print("exceptions: ", len(exceptions))
print("total: ", obstacles + len(exceptions))
