def linner_search(the_list, search):
    list_len = len(the_list)
    for i in range(list_len):
        if the_list[i] == search:
            print(f"Target: {search} \n Found at index {i}")
            return
linner_search([14, 7, 22, 9, 7, 31], 22)