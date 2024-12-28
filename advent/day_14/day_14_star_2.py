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

seconds = 500
# space_width = 11
space_width = 101
# space_height = 7
space_height = 103


def to_string(positions):
    s = "\n"
    for x in range(0, space_width):
        for y in range(0, space_height):
            if (x, y) in positions:
                s += "+"
            else:
                s += " "
        s += "\n"
    return s


for s in range(0, seconds):
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
    print(s)
    print(to_string(positions))
