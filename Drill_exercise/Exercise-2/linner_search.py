def linner_search(the_list, search):
    list_len = len(the_list)
    for i in range(list_len):
        if the_list[i] == search:
            print(f"Target: {search} \n Found at index {i}")
            return
linner_search([14, 7, 22, 9, 7, 31], 22)

# n = 12

# for i in range(1, n+1):
#     for j in range(1, i):
#         print(f"{j}", end="")
#     print()
