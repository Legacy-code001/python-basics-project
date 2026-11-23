def two_sum(list_num, target):
    two_pairs = []
    pair_index = []
    for i in range(len(list_num)):
        for j in range(i + 1, len(list_num)):
            if list_num[i] + list_num[j] == target:
                two_pairs.append((list_num[i], list_num[j]))
    #             pair_index.append((i, j))
    return two_pairs
    # return pair_index

print(two_sum([2, 7, 11, 15], 9))