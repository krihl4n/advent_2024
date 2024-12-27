path = 'input.txt'

input = []

with open(path) as file:
    for x, line in enumerate(file):
        input.append(list(line.strip("\n")))

label = "     "
for i in range (0, len(input)):
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
        explore(x, y - 1, name,  checked_fields)

    if y + 1 < len(input) and input[x][y + 1] == input[x][y]:
        explore(x, y + 1, name, checked_fields)


for x, row in enumerate(input):
    for y, field_unit in enumerate(row):
        if (x, y) not in field_names:
            explore(x, y, None, [])

print()

for f in field_names:
    print("{} -> {}".format(f, field_names[f]))

for x, row in enumerate(input):
    for y, field_unit in enumerate(row):

        field_name = field_names[(x, y)]
        if field_name in field_data:
            data = field_data[field_name]
        else:
            data = (0, 0)  # area, perimeter

        area = data[0] + 1

        perimeter = data[1]
        if x == 0 or x == len(input) - 1:
            perimeter += 1

        if y == 0 or y == len(input) - 1:
            perimeter += 1

        if x + 1 < len(input) and input[x + 1][y] != field_unit:
            perimeter += 1

        if y + 1 < len(input) and input[x][y + 1] != field_unit:
            perimeter += 1

        if x - 1 >= 0 and input[x - 1][y] != field_unit:
            perimeter += 1

        if y - 1 >= 0 and input[x][y - 1] != field_unit:
            perimeter += 1

        field_data[field_name] = (area, perimeter)

result = 0

for data in field_data:
    print()
    print(data)
    print(field_data[data])
    result += field_data[data][0] * field_data[data][1]

print(result)
