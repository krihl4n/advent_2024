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
            row = []
            for c in list(line):
                if c == "O":
                    row.append("[")
                    row.append("]")
                elif c == ".":
                    row.append(".")
                    row.append(".")
                elif c == "#":
                    row.append("#")
                    row.append("#")
                elif c == "@":
                    row.append("@")
                    row.append(".")
            map.append(row)
        if map_done:
            moves += line.strip("\n")


def print_map():
    for x in map:
        for y in x:
            print(y, end="")
        print()

print_map()


def calculate_robot_position():
    for x, row in enumerate(map):
        for y, tile in enumerate(row):
            if tile == "@":
                robot_position = (x, y)
                return robot_position

def solve():

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
        elif map[desired_pos[0]][desired_pos[1]] == "[" or map[desired_pos[0]][desired_pos[1]] == "]" :
            print("have to move box")
            if direction[0] == 0:
                move_box_horizontally(direction, desired_pos)
            else:
                print("move box vertically")
                move_box_vertically(direction, desired_pos)

    def move_box_vertically(direction, desired_pos):
        nonlocal robot_position
        boxes_to_move = []
        pos = (robot_position[0] + direction[0], robot_position[1] + direction[1])

        boxes_to_move = search_for_boxes(pos, boxes_to_move, direction)

        unique_boxes = []
        for box in boxes_to_move:
            if box not in unique_boxes:
                unique_boxes.append(box)

        boxes_can_move = True
        for box in unique_boxes:
            next_field = map[box[0] + direction[0]][box[1] + direction[1]]
            if next_field != "[" and next_field != "]" and next_field != ".":
                boxes_can_move = False

        print("boxes can move:", boxes_can_move)


        boxes_to_leave_empty_space = []

        for box in unique_boxes:
            previous_field = map[box[0] - direction[0]][box[1] - direction[1]]
            if box in unique_boxes:
                boxes_to_leave_empty_space.append(box)

        if boxes_can_move:
            tmp_map = dict()
            for box in reversed(unique_boxes):
                tmp_map[ (box[0] + direction[0], box[1] + direction[1])] = map[box[0]][box[1]]
                map[box[0]][box[1]] = "."

            for box in tmp_map:
                map[box[0]][box[1]] = tmp_map[box]


            map[robot_position[0]][robot_position[1]] = "."
            map[desired_pos[0]][desired_pos[1]] = "@"
            robot_position = desired_pos


    def search_for_boxes(pos, boxes, direction):
        if map[pos[0]][pos[1]] == "[":
            boxes.append(([pos[0], pos[1]]))
            boxes.append(([pos[0], pos[1] + 1]))
            return search_for_boxes((pos[0] + direction[0], pos[1] + direction[1]), boxes, direction) + search_for_boxes((pos[0] + direction[0], pos[1] + direction[1] + 1), boxes, direction)
        elif map[pos[0]][pos[1]] == "]":
            boxes.append(([pos[0], pos[1]]))
            boxes.append(([pos[0], pos[1] - 1]))
            return search_for_boxes((pos[0] + direction[0], pos[1] + direction[1]), boxes, direction) + search_for_boxes((pos[0] + direction[0], pos[1] + direction[1] - 1), boxes, direction)
        else:
            return boxes

    def move_box_horizontally(direction, desired_pos):
        nonlocal robot_position
        boxes_to_move = []
        pos = (robot_position[0] + direction[0], robot_position[1] + direction[1])
        while True:
            if map[pos[0]][pos[1]] == "[" or map[pos[0]][pos[1]] == "]":
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

        for box in reversed(boxes_to_move):
            map[box[0] + direction[0]][box[1] + direction[1]] =  map[box[0]][box[1]]

        map[robot_position[0]][robot_position[1]] = "."
        map[desired_pos[0]][desired_pos[1]] = "@"
        robot_position = desired_pos

    robot_position = calculate_robot_position()

    for move in moves:
        print(move)
        if move == ">":
            perform_move((0, 1))
        elif move == "<":
            perform_move((0, -1))
        elif move == "^":
            print("move up")
            perform_move((-1, 0))
        elif move == "v":
            print("move down")
            perform_move((1, 0))
    print_map()

    result = 0
    for x, row in enumerate(map):
        for y, tile in enumerate(row):
            if tile == "[":
                val = 100 * x + y
                result += val

    print("result:", result)

solve()
