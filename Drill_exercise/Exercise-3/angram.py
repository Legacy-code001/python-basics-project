def check_anagram():
    first_str = input("first string: ")

    second_str = input("second_str: ")

    dict1 = {}
    dict2 = {}

    for char in first_str:
        dict1[char] = dict1.get(char, 0) + 1

    for char2 in second_str:
        dict2[char2] = dict2.get(char2, 0) + 1

    print(dict1)
    print(dict2)

    if dict1 ==  dict2:
        return "yeah"
    else:
        return "ney"
print(check_anagram()
)