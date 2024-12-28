import numpy as np

filepath = "input.txt"
#
# A: (11, 60) B: (66, 24) prize: (1452, 4560)
# A: 0 B: 22
# Button A: X+94, Y+34
class Rule:
    def __init__(self, button_a, button_b, prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __repr__(self):
        return "A: {} B: {} prize: {}".format(self.button_a, self.button_b, self.prize)


rules = []

with open(filepath) as input_file:
    button_a = None
    button_b = None
    prize = None
    for line in input_file:
        if button_a is None or button_b is None:
            idx_1 = line.find("+") + 1
            idx_2 = line.find(",", idx_1)
            value_x = int(line[idx_1:idx_2])
            idx_3 = line.find("+", idx_2) + 1
            value_y = int(line[idx_3:].strip("\n"))
            if button_a is None:
                button_a = (value_x, value_y)
            else:
                button_b = (value_x, value_y)
        elif prize is None:
            idx_1 = line.find("=") + 1
            idx_2 = line.find(",", idx_1)
            value_x = int(line[idx_1:idx_2])
            idx_3 = line.find("=", idx_2) + 1
            value_y = int(line[idx_3:].strip("\n"))
            prize = (value_x, value_y)
        else:
            rules.append(Rule(button_a, button_b, prize))
            button_a = None
            button_b = None
            prize = None
    rules.append(Rule(button_a, button_b, prize))


def solve_iterative(rule):
    print("iterative")
    ax = rule.button_a[0]
    ay = rule.button_a[1]

    bx = rule.button_b[0]
    by = rule.button_b[1]

    px = rule.prize[0]
    py = rule.prize[1]

    x = px
    y = py

    a_count = 0
    b_count = 0

    solved = False
    while x > 0:
        if x % bx == 0 and y % by == 0 and int(x / bx) == int(y / by):
            b_count = int(x / bx)
            solved = True
            break
        else:
            x -= ax
            y -= ay
            a_count += 1

    if solved:
        print("A: {} B: {}".format(a_count, b_count))
        return True
    else:
        print("unsolvable")
        return False


def solve_with_algebra(rule):
    print("algebra")
    ax = rule.button_a[0]
    ay = rule.button_a[1]

    bx = rule.button_b[0]
    by = rule.button_b[1]

    px = rule.prize[0]
    py = rule.prize[1]

    A = np.array([[ax, bx], [ay, by]])
    b = np.array([px, py])
    x = np.linalg.solve(A, b)

    a_count_f = x[0]
    b_count_f = x[1]
    print(x)

    x = x.astype(np.int64)
    a_count_i = x[0]
    b_count_i = x[1]

    diff_a = abs(a_count_f - a_count_i)
    diff_b = abs(b_count_f - b_count_i)

    print(diff_a, diff_b)
    precision = 0.001
    if (diff_a < precision or 1 - diff_a < precision) and (diff_b < precision or 1 - diff_b < precision):
        print("solved")
        if 1 - diff_b < precision:
            b_count_i += 1
        if 1 - diff_a < precision:
            a_count_i += 1
        print(a_count_i, b_count_i)
        return True
    else:
        print("unsolvable")
        return False


for rule in rules:
    print()
    print(rule)

    r1 = solve_iterative(rule)
    r2 = solve_with_algebra(rule)

    if r1 is not r2:
        print("difference found!")
