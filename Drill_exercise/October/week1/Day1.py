#Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.

# Given Input: List: [1, 2, 3, 4, 5], Shift: 2, Direction: 'right'

# Expected Output: [4, 5, 1, 2, 3]


def rotate(lst, n, direction):
    if not lst:
        return lst

    n = n % len(lst)

    if direction == "right":
        return lst[-n:] + lst[:-n]
    else:
        return lst[n:] + lst[:n]

# print(rotate([1, 2, 3, 4, 5], 2, "left"))


# 2. Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.

# Given Input: d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4}

# Expected Output: {'a': [1], 'b': [2, 3], 'c': [4]}

def merge_dict(dict1, dict2):
    merge_dict = {}

    the_keys = set(dict1.keys()) | set(dict2.keys())

    for key in the_keys:
        values = []
        if key in dict1.keys():
            values.append(dict1[key])
        if key in dict2.keys():
            values.append(dict2[key])
        merge_dict[key] = values
    return merge_dict

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dict(d1, d2))

    # for val in dict1:
    #     if not merge_dict[val]:
    #         return marge_dict[val] = []
    #     else:
    #         return marge_dict[val] = dict1[val]

