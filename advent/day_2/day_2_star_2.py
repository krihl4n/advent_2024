
filepath = "input.txt"

def to_ints(array):
    result = []
    for el in array:
        result.append(int(el))
    return result

with open(filepath) as file:
    safe_reports = 0

    corrected_reports = []
    bad_reports = []

    for line in file:
        report_safe = False

        levels = to_ints(line.split(" "))

        should_increase = levels[0] < levels[1]
                
        for idx, level in enumerate(levels):
            if(idx + 1) == len(levels):
                report_safe = True
                break

            next_level = levels[idx+1]

            increases = level < next_level
            if (not increases and should_increase) or (increases and not should_increase):
                tmp_1 = levels.copy()
                tmp_2 = levels.copy()
                tmp_3 = levels.copy()
                if idx-1 >= 0:
                    del tmp_3 [idx-1]
                del tmp_1[idx]
                del tmp_2[idx+1]
                corrected_reports.append((tmp_1,tmp_2,tmp_3,levels))
                break
            
            diff = abs(level - next_level)
            if(diff < 1 or diff > 3):
                tmp_1 = levels.copy()
                tmp_2 = levels.copy()
                tmp_3 = levels.copy()
                if idx-1 >= 0:
                    del tmp_3 [idx-1]
                del tmp_1[idx]
                del tmp_2[idx+1]
                corrected_reports.append((tmp_1,tmp_2,tmp_3,levels))
                break

        if report_safe:
            safe_reports += 1
    

    print("safe reports without correction:")
    print(safe_reports)

    # corrected
    for report_pair in corrected_reports:
        report_safe = False

        for levels in report_pair:
            should_increase = levels[0] < levels[1]

            for idx, level in enumerate(levels):
                if(idx + 1) == len(levels):
                    report_safe = True
                    break

                next_level = levels[idx+1]

                increases = level < next_level
                if (not increases and should_increase) or (increases and not should_increase):
                    break
                
                diff = abs(level - next_level)
               # print("diff: ", diff)
                if(diff < 1 or diff > 3):
                    break

            if report_safe:
                safe_reports += 1
                break
            else:
                bad_reports.append(levels)

    print("safe reports with correction:")
    print(safe_reports)
    # print("bad reports:")
    # print(bad_reports)

        