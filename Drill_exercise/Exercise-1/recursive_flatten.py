def flatten(val):
    val_list = []
    for i in val:
        if isinstance(i, list):
            val_list.extend(flatten(i))
        else:
            val_list.append(i)
    return val_list

# deep_list = [1, [2, 3], [[4, 5], 6]]
# print(flatten(deep_list))



def group_by(items, key_fn):
    '''group item from an iterable into a fresh dictionary using key_fn'''
    results = {}
    for item in items:
        key = key_fn(item)
        if key not in results:
            results[key] = [item]
        else:
            results[key].append(item)
    return results


def combined(nested_word):
    """flatten a listen list of word and group them by their first letter"""
    flat_words = flatten(nested_word)
    return group_by(flat_words, lambda x: x[0] if x else "")


print(combined([["apple", "avocade"], ["banana"], [["cherry"]]]))