from time import sleep

path = 'input.txt'


class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return "p = {} {} v = {} {}".format(self.px, self.py, self.vx, self.vy)


robots = []

with open(path) as file:
    for line in file:
        idx_1 = line.find("=")
        idx_2 = line.find(",", idx_1)
        idx_3 = line.find(" ", idx_2)
        idx_4 = line.find("=", idx_3)
        idx_5 = line.find(",", idx_4)

        px = int(line[idx_1 + 1:idx_2])
        py = int(line[idx_2 + 1:idx_3])

        vx = int(line[idx_4 + 1: idx_5])
        vy = int(line[idx_5 + 1:])

        robot = Robot(px, py, vx, vy)
        robots.append(robot)
        # print(robot)

seconds = 10000
# space_width = 11
space_width = 101
# space_height = 7
space_height = 103


def to_string(positions):
    s = "\n"
    for x in range(0, space_width):
        for y in range(0, space_height):
            if (x, y) in positions:
                s += "O"
            else:
                s += " "
        s += "\n"
    return s

#
# def to_string(positions):
#     s = "\n"
#     for x in range(0, space_width):
#         for y in range(0, space_height):
#             if (y, x) in positions:
#                 s += "O"
#             else:
#                 s += " "
#         s += "\n"
#     return s


def append_text_to_file(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')

    except Exception as e:
        print(e)


n = 9996
for s in range(0, 8000):
    positions = []

    for robot in robots:
        px = robot.px
        py = robot.py

        px += robot.vx
        py += robot.vy

        if px < 0:
            px += space_width

        if px >= space_width:
            px -= space_width

        if py < 0:
            py += space_height

        if py >= space_height:
            py -= space_height

        positions.append((px, py))
        robot.px = px
        robot.py = py

    img = to_string(positions)
    print(s)
    if "OOOOOOOOOOOO" in img:
        to_append = "{}\n{}\n\n".format(s, img)
        append_text_to_file("result.txt", to_append)

    # # times = [805, 906, 1007, 1108, 1209, 1310, 1411, 1512, 1613, 1714, 1815, 1916]
    # times = [1916, 2017, 2118, 2219, 2320, 2421, 2522, 2623, 2724, 2825, 2926]
    #
    # if s == n:
    #     n = 101 + n
    #     print(s)
    #     image = to_string(positions)
    #
    #     to_append = "{}\n{}\n\n".format(s, image)
    #     append_text_to_file("result.txt", to_append)
        # print(image[:int(len(image)/2)])
        # sleep(0.1)

#7370 -- wrong
#7371 -- wrong
#17773
#17774 - tried

