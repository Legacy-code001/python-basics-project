# Practice Problem: Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.

# Given Input: list1 = [101, 102, 103], list2 = [103, 104, 105]

# Expected Output: {101, 102, 104, 105}

# Performance: Like all set operations in Python, this is executed in O(n) time, making it efficient for thousands of entries

def single_appear(a, b):
    return a.union(b)

list1 = [101, 102, 103]
list2 = [103, 104, 105]

print(single_appear(set(list1), set(list2)))


# 2

# Exercise 16: Power Set Generation
# Practice Problem: Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).

# Use itertools.combinations in a loop that varies the size of the subset from 0 to the length of the list.z
from itertools import combinations
def possible_set(set_sample):

    elements = list(set_sample)
    power_set = []
    
    for r in range(len(elements) + 1):
        # Generate all combinations of length r
        for combo in combinations(elements, r):
            power_set.append(combo)
            
    return power_set

my_set = {1, 2, 3}
print(possible_set(my_set))

# combinations(elements, r): This built-in function generates all possible ways to pick r items from the list without repetition and regardless of order.
# range(len(elements) + 1): We start at 0 to include the Empty Set () and go up to the full length to include the original set.
# Growth: Keep in mind that the power set of a set with N elements has 2n subsets. For 3 elements, you get 8 subsets; for 10 elements, you get 1,024

# strptime: This function converts a string into a datetime object based on a format code (%Y for 4-digit year, etc.).
# relativedelta: Unlike a standard timedelta (which only tracks days and seconds), relativedelta understands the calendar and can correctly calculate years and months while accounting for leap years.
# Error Handling: The try/except block ensures that if a user types an impossible date (like “1995-02-30”), the program provides a helpful error instead of crashing.from dateutil.relativedelta import relativedelta

def present_date(birthdaystr):
    try:
        birthday = datetime.strptime(birthdaystr, "%Y-%m-%d").date()

        present_daytime = datetime.now().date()

        diff = relativedelta(present_daytime, birthday)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

Bd = "1995-05-15"
print(present_date(Bd))



         