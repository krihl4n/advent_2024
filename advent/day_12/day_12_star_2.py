path = 'input.txt'

input = []

with open(path) as file:
    for x, line in enumerate(file):
        input.append(list(line.strip("\n")))

label = "     "
for i in range(0, len(input)):
    label += "{}    ".format(i)

print(label)
for i, el in enumerate(input):
    print("{}  {}".format(i, el))

field_data = dict()
field_names = dict()


def explore(x, y, name, checked_fields):
    if x < 0 or y < 0 or x == len(input) or y == len(input):
        return

    if name is None:
        name = "{}_{}_{}".format(input[x][y], x, y)

    if (x, y) in checked_fields:
        return

    checked_fields.append((x, y))
    field_names[(x, y)] = name

    if x - 1 >= 0 and input[x - 1][y] == input[x][y]:
        explore(x - 1, y, name, checked_fields)

    if x + 1 < len(input) and input[x + 1][y] == input[x][y]:
        explore(x + 1, y, name, checked_fields)

    if y - 1 >= 0 and input[x][y - 1] == input[x][y]:
        explore(x, y - 1, name, checked_fields)

    if y + 1 < len(input) and input[x][y + 1] == input[x][y]:
        explore(x, y + 1, name, checked_fields)


for x, row in enumerate(input):
    for y, field_unit in enumerate(row):
        if (x, y) not in field_names:
            explore(x, y, None, [])

print()

for f in field_names:
    print("{} -> {}".format(f, field_names[f]))


class Side:
    def __init__(self, coord1, coord2, changing_coord, horizontal):
        self.coord1 = coord1
        self.coord2 = coord2
        self.changing_coord = changing_coord
        self.horizontal = horizontal

    def __eq__(self, other):
        return self.coord1 == other.coord1 and self.coord2 == other.coord2 and self.horizontal == other.horizontal and self.changing_coord == other.changing_coord

    def __repr__(self):
        return "{} {} {} {}".format(self.coord1, self.coord2, self.changing_coord, self.horizontal)


for x, row in enumerate(input):
    for y, field_unit in enumerate(row):

        field_name = field_names[(x, y)]
        if field_name in field_data:
            data = field_data[field_name]
        else:
            data = (0, [])  # area, perimeter

        area = data[0] + 1

        sides = data[1]
        if x == 0:
            sides.append(Side(-1, x, y, False))
        if x == len(input) - 1:
            sides.append(Side(len(input), x, y, False))

        if y == 0:
            sides.append(Side(-1, y, x, True))
        if y == len(input) - 1:
            sides.append(Side(len(input), y, x, True))

        if x + 1 < len(input) and input[x + 1][y] != field_unit:
            sides.append(Side(x + 1, x, y, False))

        if y + 1 < len(input) and input[x][y + 1] != field_unit:
            sides.append(Side(y + 1, y, x, True))

        if x - 1 >= 0 and input[x - 1][y] != field_unit:
            sides.append(Side(x - 1, x, y, False))

        if y - 1 >= 0 and input[x][y - 1] != field_unit:
            sides.append(Side(y - 1, y, x, True))

        field_data[field_name] = (area, sides)

result = 0


def process_sides(sides):
    processed_sides = []

    for i, s in enumerate(sides):
        processed_side = [s]

        counter = 1
        next_side = Side(s.coord1, s.coord2, s.changing_coord + counter, s.horizontal)
        while next_side in sides:
            processed_side.append(next_side)
            counter += 1
            next_side = Side(s.coord1, s.coord2, s.changing_coord + counter, s.horizontal)

        counter = -1
        prev_side = Side(s.coord1, s.coord2, s.changing_coord + counter, s.horizontal)
        while prev_side in sides:
            processed_side.insert(0, prev_side)
            counter -= 1
            prev_side = Side(s.coord1, s.coord2, s.changing_coord + counter, s.horizontal)

        if processed_side not in processed_sides:
            processed_sides.append(processed_side)

        print("processed: ", processed_sides)
    print(len(processed_sides))
    return len(processed_sides)


for data in field_data:
    print()
    print(data)
    print(field_data[data])
    result += field_data[data][0] * process_sides(field_data[data][1])

print(result)
