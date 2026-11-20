# Practice Problem: Create a function that takes a start date and an integer N, then calculates the date exactly N business days (Monday–Friday) in the future.

from datetime import datetime, timedelta


# date = datetime.date.today()
# print(date)
# print(type(date))

def get_date(present_data, n):
    current_date = present_data
    days_time = 0

    while days_time < n:
        current_date += timedelta(days=1)

        if current_date.weekday() < 5:
            days_time += 1
    
    return current_date

present_date_my = datetime(2026, 1, 3)
result = get_date(present_date_my, 5)
print(f"present_date_my: {present_date_my.strftime('%A, %Y-%m-%d')}")
print(f"the businessday in N days: {result.strftime('%A, %Y-%m-%d')}")


#20 Practice Problem: Create a class PowerOfTwo that allows you to iterate through powers of 2 (1, 2, 4, 8…) up to a specified maximum exponent.

class Power_Of_Two():
    def __init__(self, max_exponent):
        self.max = max_exponent
        self.n = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
    
for val in Power_Of_Two(3):
    print(val)


# 21 Practice Problem: Write a function that identifies all duplicate elements in a list. The solution must run in linear time, meaning you should only traverse the list once.

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

# Expected Output: Duplicates found: {1, 2}


seen = set()
duplicate = set()

for val in numbers:
    if val in seen:
        duplicate.add(val)
    else:
        seen.add(val)
print(duplicate)
