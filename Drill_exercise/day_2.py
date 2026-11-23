"""Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
4 Anagram"""


# # def check_for_anagram():
# #     firstVal = input("first: ")
# #     secondVal = input("first: ")

# #     first_dict = {}
# #     second_dict = {}

# #     for val in firstVal:
# #         first_dict[val] = first_dict.get(val, 0) + 1
        

# #     for val in secondVal:
# #         second_dict[val] = second_dict.get(val, 0) + 1

# #     return first_dict == second_dict

# # print(check_for_anagram())

# #or

# def is_anagram(str1, str2):
#     # Clean and sort both strings
#     s1 = sorted(str1.lower().replace(" ", ""))
#     s2 = sorted(str2.lower().replace(" ", ""))
    
#     # If the sorted lists are identical, they are anagrams
#     return s1 == s2

# w1, w2 = "listen", "silent"
# result = is_anagram(w1, w2)

# print(f'Is "{w1}" an anagram of "{w2}"? {result}')

#5.Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.

def flatten_list(given_list):
    flat_list = []
    for val in given_list:
        if isinstance(val, list):
            flat_list.extend(flatten_list(val))
        else:
            flat_list.append(val)
    return flat_list

print(flatten_list([1, [2, 3], [4, [5, 6]], 7]))
    

