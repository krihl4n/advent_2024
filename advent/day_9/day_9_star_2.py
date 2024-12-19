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


i = len(disk_map) - 1

while i >= 0:
    if disk_map[i].isnumeric():
        file_id = disk_map[i]
        j = i
        file_size = 0
        while disk_map[j] == file_id and j >= 0:
            file_size += 1
            j -= 1
        #print("size:", file_size)

        i -= file_size

        for k in range(0,i):
            if disk_map[k] == '.':
                kk = k
                space = 0
                while disk_map[kk] == '.':
                    space += 1
                    kk += 1

                kk = k

                if space >= file_size:
                    c1 = file_size
                    while c1 > 0:
                        disk_map[kk] = file_id
                        kk += 1
                        c1 -= 1

                    c2 = file_size
                    tmp_i = i + 1
                    while c2 > 0:
                        disk_map[tmp_i] = '.'
                        tmp_i += 1
                        c2 -= 1
                    break

    else:
        i -= 1

print(disk_map)
checksum = 0
for i, block in enumerate(disk_map):
    if block.isnumeric():
        checksum += (i * int(block))
    else:
        continue

print("checksum: ", checksum)
print()
# 0099811188827773336446555566..............


# 91380424522

# 0000........1111111.....2222222........333333333......4444.5555...6666....777777.......8888888.9
# 0000999999991111111999992222222999999993333333339999994444955559996666999977
