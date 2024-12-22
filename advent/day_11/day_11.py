input = "17"
#input = "125 17"
#input = "17639 47 3858 0 470624 9467423 5 188"

stones = input.split(" ")
print(stones)

for i in range(0, 75):
    modified_stones = []
    for stone in stones:
        if int(stone) == 0:
            modified_stones.append("1")
        elif len(stone) % 2 == 0:
            first = stone[:int(len(stone) / 2)]
            second = stone[int(len(stone) / 2):]
            modified_stones.append(first)
            modified_stones.append(str(int(second)))
        else:
            mod = 2024 * int(stone)
            modified_stones.append(str(mod))

    #print(modified_stones)
    stones = modified_stones
    print("pass {}: {}".format(i + 1, len(stones)))

result = len(stones)
print("stones:", result)
