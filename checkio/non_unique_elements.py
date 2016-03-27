def checkio(data):
    #data = [10, 9, 10, 10, 9, 8]
    count_dict = {}
    non_uniques = []
    for count in data:
        count_dict[count] = count_dict.get(count, 0) + 1
    for nonunique in count_dict.items():
        if nonunique[1] == 1:
            data.remove(nonunique[0])
    return data