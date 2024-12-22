#input = "17"
#input = "125 17"
input = "17639 47 3858 0 470624 9467423 5 188"

stones = input.split(" ")
print(stones)

already_calculated = dict()

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

for i in range(0, 75):
    modified_stones = []
    cache_hit = 0
    for stone in stones:
        if stone in already_calculated:
            modified = already_calculated[stone]
            cache_hit += 1
        else:
            modified = modify_stone(stone)
            already_calculated[stone] = modified
        modified_stones += modified

    #print(modified_stones)
    stones = modified_stones
    print("pass {}: {}".format(i + 1, len(stones)))
    print("cache hit:", cache_hit)

result = len(stones)
print("stones:", result)
