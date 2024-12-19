path = 'input.txt'

print()

with open(path) as file:
    input = file.readline()

print(input)

disk_map = []
is_file = True
file_id = 0

for block_representation in input:
    number_of_blocks = int(block_representation)
    if is_file:
        for i in range(0, number_of_blocks):
            disk_map.append(str(file_id))
        file_id += 1
        is_file = False

    else:
        for i in range(0, number_of_blocks):
            disk_map += '.'
        is_file = True

print(disk_map)
modified_map = []

last_index = len(disk_map) - 1

number_of_dots = 0
for block in disk_map:
    if block == '.':
        number_of_dots += 1

print("dots:", number_of_dots)
for i, block in enumerate(disk_map):
    if i >= len(disk_map) - number_of_dots:
        modified_map.append('.')
        continue
    if block != '.':
        modified_map.append(block)
    else:
        for i in range(last_index, 0, -1):
            last_index -= 1
            if disk_map[i] == '.':
                continue
            else:
                modified_map.append(disk_map[i])
                break

print(modified_map)

checksum = 0
for i, block in enumerate(modified_map):
    if block.isnumeric():
        checksum += (i * int(block))
    else:
        break

print("checksum: ", checksum)
print()
# 0099811188827773336446555566..............


# 91380424522

# 0000........1111111.....2222222........333333333......4444.5555...6666....777777.......8888888.9
# 0000999999991111111999992222222999999993333333339999994444955559996666999977
