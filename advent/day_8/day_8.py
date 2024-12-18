
points = [(3, 4), (5, 5)]

def find_antinodes_for(point_1, point_2):
    dist_x = abs(point_1[0] - point_2[0])
    dist_y = abs(point_1[1] - point_2[1])

    res_x1 = point_1[0]
    res_x2 = point_1[0]
    if point_1[0] < point_2[0]:
        res_x1 = point_1[0] - dist_x
        res_x2 = point_2[0] + dist_x
    elif point_1[0] > point_2[0]:
        res_x1 = point_2[0] - dist_x
        res_x2 = point_1[0] + dist_x

    res_y1 = point_1[1]
    res_y2 = point_1[1]

    if point_1[1] < point_2[1]:
        res_y1 = point_1[1] - dist_y
        res_y2 = point_2[1] + dist_y
    elif point_2[1] > point_1[1]:
        res_y1 = point_2[1] - dist_y
        res_y2 = point_1[1] + dist_y

    return [(res_x1, res_y1), (res_x2, res_y2)]

print(find_antinodes_for((3, 4), (5, 5))) # expected (1, 3) (7, 6)
