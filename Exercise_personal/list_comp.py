# """
# Exercise Purpose: List comprehensions are a hallmark of Pythonic code. They allow you to replace verbose for loops and .append() calls with a readable, optimized single line. This exercise teaches you how to combine transformation (uppercase) and filtering (length check) in one expression.

# Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

# Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
# """

# words = ["apple", "bat", "cherry", "dog", "elderberry"]

# word_output = [word.upper() for word in words if len(word) >= 4]

# print(word_output)



# """2. 
# Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}

# Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

# """



# dict_a = {'a': 10, 'b': 20} 

# dict_b = {'b': 5, 'c': 15}

# dict_a.update(dict_b)
# for i in dict_b.keys():
#     if i not in dict_a:
#         dict_a[i] = dict_b[i]
    

# print(dict_a)

# def merge_dicts(d1, d2):
#     # Start with a copy of d1 to avoid modifying the original
#     result = d1.copy()
    
#     for key, value in d2.items():
#         # .get(key, 0) returns 0 if the key doesn't exist yet
#         result[key] = result.get(key, 0) + value
    
#     return result

# dict_a = {'a': 10, 'b': 20}
# dict_b = {'b': 5, 'c': 15}

# merged = merge_dicts(dict_a, dict_b)
# print(f"Merged Dictionary: {merged}")


"""
Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.
"""

def count_charcter():
    input_value = input("value: ")

    dict_value = {}
    for val in input_value.strip():
        dict_value[val] = dict_value.get(val, 0) + 1
    return dict_value

print(count_charcter())