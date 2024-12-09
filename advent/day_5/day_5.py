filepath = "input.txt"

before_rules = dict()

rules_done = False
updates = []
with open(filepath) as input_file:
    for line in input_file:
        if not rules_done:
            if line == "\n":
                rules_done = True
                continue
            nums = line.replace("\n", "").split("|")
            key = int(nums[0])
            val = int(nums[1])

            new_vals = [val]
            if key in before_rules:
                new_vals += before_rules[key]
            before_rules[key] = new_vals

        else:
            updates.append(line.replace("\n", "").split(","))
print("rules:", before_rules)
print(updates)

sum = 0

incorrect_updates = []

for idx_u, update in enumerate(updates):
    update_correct = True

    for idx_p, page in enumerate(update):
        page = int(page)
        page_rules = []
        if page in before_rules:
            page_rules = before_rules[page]
        #print("page rules:", page_rules)
        for idx_pc in range(0, idx_p):
            if int(update[idx_pc]) in page_rules:
                update_correct = False
                break
        if not update_correct:
            incorrect_updates.append(update)
            break
    print("update:", update)
    print("correct:", update_correct)
    if update_correct:
        size = len(update)
        middle = int(size/2)
        num = int(update[middle])
        print("num:", num)
        sum += num

print(sum)
print(incorrect_updates)

fixed_sum = 0
for idx, incorrect_update in enumerate(incorrect_updates):
    fixed_update = []
    for idy, incorrect_page in enumerate(incorrect_update):
        incorrect_page = int(incorrect_page)
        index_to_insert = 0

        for idz, correct_page in enumerate(fixed_update):
            correct_page = int(correct_page)
            before_rules_for_page = before_rules.get(incorrect_page, [])
            if correct_page in before_rules_for_page:
                index_to_insert = idz
                break
            index_to_insert += 1

        fixed_update.insert(index_to_insert, incorrect_page)

    print("fixed:", fixed_update)
    size = len(fixed_update)
    middle = int(size / 2)
    num = int(fixed_update[middle])
    print("num:", num)
    fixed_sum += num

print("fixed sum", fixed_sum)
