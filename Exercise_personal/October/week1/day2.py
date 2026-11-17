# Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.

# Given Input:

# {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
# Expected Output:

# {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}

def invert(dict):
    return_dict = {}

    for key, val in dict.items():
        for v in val:
            return_dict[v] = key

    return return_dict 

d = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
print(invert(d))


# Quest2
# Practice Problem: Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function
#     employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]
# Expected Output:

# [{'name': 'B', 'salary': 70}, {'name': 'C', 'salary': 60}, {'name': 'A', 'salary': 50}]
# Use sorted(list, key=lambda x: x['key_name'], reverse=True)
employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]
sort_salary = sorted(employees, key=lambda x: x["salary"], reverse=True )
print(sort_salary)

# quest 3
# Practice Problem: Write a script that takes two lists of integers from a user, converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.

# Given Input: Set A: {1, 2, 3}, Set B: {1, 2, 3, 4, 5}

# Expected Output: Set A is a subset of Set B

def checks_sets(sat_a, set_b):
    if set_a.issubset(set_b):
        print(f"set_a {set_a} is a subset of {set_b}")
    elif set_a.issperset(set_b):
        print(f"set_a {set_a} is a super of {set_b}")
    elif:
        if a.isdisjoint(b):
        print("The sets are disjoint (they share no elements).")
    else:
        print(f"The sets share these elements: {a & b}")

