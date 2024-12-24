#input = "17"
#input = "125 17"
input = "17639 47 3858 0 470624 9467423 5 188"

stones = input.split(" ")
print(stones)

cache = {}

# https://www.geeksforgeeks.org/memoization-using-decorators-in-python/

def memoize_count(f):
        def inner(stone, number):
            if (stone, number) not in cache:
                cache[(stone, number)] = f(stone, number)
            return cache[(stone, number)]
        return inner

@memoize_count
def count(stone, number):
    if number == 0:
        return 1
    if int(stone) == 0:
        return count("1", number-1)
    elif len(stone) % 2 == 0:
        first = stone[:int(len(stone) / 2)]
        second = stone[int(len(stone) / 2):]
        return count(first, number-1) + count(str(int(second)), number-1)
    else:
        return count(str(2024 * int(stone)), number-1)

result = 0
for s in stones:
    print("processing:", s)
    result += count(s, 75)

print("result:", result)
