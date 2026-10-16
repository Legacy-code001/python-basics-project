def smallest(given_list):
    smallest = given_list[0]
    list_len = len(given_list)
    if list_len == 1:
        return given_list[0]
    for i in range(1, list_len - 1):
        if given_list[i] < smallest:
            smallest = given_list[i]
    return smallest


def largest(given_list):
    largest = given_list[0]
    list_len = len(given_list)
    if list_len == 1:
        return given_list[0]
    for i in range(1, list_len - 1):
        if given_list[i] > largest:
            largest = given_list[i]
    return largest

def total(given_list):
    cumm = given_list[0]
    list_len = len(given_list)
    if list_len == 1:
        return given_list[0]
    for i in range(1, list_len-1):
        cumm += given_list[i]
    return cumm

def avg(given_list):
    list_len = len(given_list)
    if list_len == 1:
        return given_list[0]
    list_avg = total(given_list)/list_len
    return list_avg

def analyse_list(the_list):
    print(f"Smallest: {smallest(the_list)}")
    print(f"Largest: {largest(the_list)}")
    print(f"Total: {total(the_list)}")
    print(f"Average: {avg(the_list)}")

analyse_list([12])

