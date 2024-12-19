path = 'advent/day_9/test_input.txt'

print()

with open(path) as file:
    input = file.readline()

print(input)

disk_map = ""

is_file = True
file_id = 0

for block_representation in input:
    number_of_blocks = int(block_representation)
    if is_file:
        for i in range(0, number_of_blocks):
            disk_map += str(file_id)
        file_id += 1
        is_file = False

    else:
        for i in range(0, number_of_blocks):
            disk_map += '.'
        is_file = True

print(disk_map)

modified_map = ""

last_index = len(disk_map) - 1

for block in disk_map:
    if block != '.':
        modified_map += block
    else:
        for i in range(last_index, 0, -1):
            if disk_map[i] == '.':
                continue
            else:
                modified_map += disk_map[i]
                last_index -= 1
                


print(modified_map)
print()
