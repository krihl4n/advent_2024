
filepath = "advent/day_2/input.txt"

def to_ints(array):
    result = []
    for el in array:
        result.append(int(el))
    return result

with open(filepath) as file:
    safe_reports = 0

    for line in file:
        report_safe = False

        levels = to_ints(line.split(" "))
        print(levels)

        should_increase = levels[0] < levels[1] # todo escape it equal
        
        for idx, level in enumerate(levels):
            if(idx + 1) == len(levels):
                report_safe = True
                break

            next_level = levels[idx+1]

            increases = level < next_level
            if (not increases and should_increase) or (increases and not should_increase):
                break
            
            diff = abs(level - next_level)
            if(diff < 1 or diff > 3):
                break

        if report_safe:
            safe_reports += 1
    
    print("safe reports:")
    print(safe_reports)





        