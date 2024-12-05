filepath = "input.txt"


with open(filepath) as input_file:

    list1 = []
    list2 = []
    distances = []
    total_distance = 0

    for line in input_file:
        pair = line.split()
        list1.append(pair[0])
        list2.append(pair[1])

    list1.sort()
    list2.sort()

    # print(list1)
    # print(list2)

    for idx, el in enumerate(list1):
        distance = abs(int(list1[idx]) - int(list2[idx]))
        total_distance += distance
    
    print("total distance:")
    print(total_distance)    

    similarity = 0
    for el in list1:
        similarity += (int(el)*list2.count(el))

    print("similarity:")
    print(similarity)