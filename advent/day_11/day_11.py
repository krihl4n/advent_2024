#input = "17"
input = "125 17"
#input = "17639 47 3858 0 470624 9467423 5 188"

stones = input.split(" ")
print(stones)


def modify_stone(stone):
    ms = []
    if int(stone) == 0:
        ms.append("1")
    elif len(stone) % 2 == 0:
        first = stone[:int(len(stone) / 2)]
        second = stone[int(len(stone) / 2):]
        ms.append(first)
        ms.append(str(int(second)))
    else:
        mod = 2024 * int(stone)
        ms.append(str(mod))
    return ms

for i in range(0, 25):
    modified_stones = []
    for stone in stones:
        modified = modify_stone(stone)
        modified_stones += modified

    #print(modified_stones)
    stones = modified_stones
    # print("pass {}: {}".format(i + 1, len(stones)))
    # print(stones)

result = len(stones)
# print(stones)
print("stones:", result)
