filepath = "input.txt"

map_done = False

map = []
moves = ""

with open(filepath) as file:
    for line in file:
        if line == "\n":
            map_done = True
            continue
        if not map_done:
            map.append(list(line))
        if map_done:
            moves += line.strip("\n")


def print_map():
    for x in map:
        for y in x:
            print(y, end="")


print_map()


def solve():
    robot_position = None
    for x, row in enumerate(map):
        for y, tile in enumerate(row):
            if tile == "@":
                robot_position = (x, y)

    def perform_move(direction):
        nonlocal robot_position
        desired_pos = (robot_position[0] + direction[0], robot_position[1] + direction[1])
        if map[desired_pos[0]][desired_pos[1]] == "#":
            print("wall")
        elif map[desired_pos[0]][desired_pos[1]] == ".":
            print("free to move")
            map[robot_position[0]][robot_position[1]] = "."
            map[desired_pos[0]][desired_pos[1]] = "@"
            robot_position = desired_pos
        elif map[desired_pos[0]][desired_pos[1]] == "O":
            print("have to move box")
            boxes_to_move = []

            pos = (robot_position[0] + direction[0], robot_position[1] + direction[1])
            while True:
                if map[pos[0]][pos[1]] == "O":
                    boxes_to_move.append((pos[0], pos[1]))
                elif map[pos[0]][pos[1]] == "#":
                    print("cannot move")
                    boxes_to_move = []
                    desired_pos = robot_position
                    break
                else:
                    print("found free space")
                    break
                pos = (pos[0] + direction[0], pos[1] + direction[1])

            for box in boxes_to_move:
                map[box[0] + direction[0]][box[1] + direction[1]] = "O"

            map[robot_position[0]][robot_position[1]] = "."
            map[desired_pos[0]][desired_pos[1]] = "@"
            robot_position = desired_pos

    for move in moves:
        print(move)
        if move == ">":
            perform_move((0, 1))
        elif move == "<":
            perform_move((0, -1))
        elif move == "^":
            perform_move((-1, 0))
        elif move == "v":
            perform_move((1, 0))
    print_map()

    result = 0
    for x, row in enumerate(map):
        for y, tile in enumerate(row):
            if tile == "O":
                val = 100 * x + y
                result += val

    print("result:", result)
solve()

#10092