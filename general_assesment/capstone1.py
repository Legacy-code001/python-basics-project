records = [
    ("ST01", "Python"),
    ("ST02", "HTML"),
    ("ST01", "Python"),
    ("ST03", "CSS"),
    ("ST02", "HTML"),
    ("ST01", "JavaScript"),
    ("ST03", "CSS"),
    ("ST01", "Python"),
]



def analyse_records():
    student_count = {}
    activity_count = {}

    for i, val in records:
        student_count[i] = student_count.get(i, 0) + 1
        activity_count[val] = activity_count.get(val, 0) + 1

    return student_count, activity_count

print(analyse_records())


def count_student_records(record, id):

    while record >= 0:
        each = []
        for item in range(len(analyse_records())):
            each.append(analyse_records()[item])
        print(each)

        for i,v in each.items():
            if i == id:
                if v == 0:
                    return 0
                else:
                    print(f"{record}")
                    return count_student_records(record - 1, id)
            else:
                return "record do not exits"
print(count_student_records(4, "ST01",))
    
# print(count_student_records())
print("anser")





import functools

def track_calls(func):
    @functools.wraps(func)  # Keeps the original function's name and docstring
    def wrapper(*args, **kwargs):
        # 1 & 5. Increment the persistent counter across separate calls
        wrapper.calls += 1
        
        # 4. Print the current count clearly
        print(f"📢 [Decorator] '{func.__name__}' has been called {wrapper.calls} time(s).")
        
        # 2 & 3. Accept any args/kwargs and return the original function's result unchanged
        return func(*args, **kwargs)
    
    # 4. Initialize the counter as an attribute on the wrapper so it's accessible externally
    wrapper.calls = 0
    return wrapper


# Applying the decorator to analyze_records
@track_calls
def analyze_records(data_list):
    student_count = {}
    for student, activity in data_list:
        student_count[student] = student_count.get(student, 0) + 1
    return student_count

# --- Testing the Implementation ---

# Call 1
res1 = analyze_records(records)
print("Result 1:", res1)
print(f"External Counter Check: {analyze_records.calls}\n" + "-"*40)

# Call 2 (Demonstrating keyword arguments)
res2 = analyze_records(data_list=records)
print("Result 2:", res2)
print(f"External Counter Check: {analyze_records.calls}\n" + "-"*40)

=======
records = [
    ("ST01", "Python"),
    ("ST02", "HTML"),
    ("ST01", "Python"),
    ("ST03", "CSS"),
    ("ST02", "HTML"),
    ("ST01", "JavaScript"),
    ("ST03", "CSS"),
    ("ST01", "Python"),
]



def analyse_records():
    student_count = {}
    activity_count = {}

    for i, val in records:
        student_count[i] = student_count.get(i, 0) + 1
        activity_count[val] = activity_count.get(val, 0) + 1

    return student_count,activity_count

print(analyse_records())


def count_student_records(record, id):

    while record >= 0:
        each = []
        for item in range(len(analyse_records())):
            each.append(analyse_records()[item])

        first = each[0]
        print(first)
    
        for i,v in first.items():
            if i == id:
                if v == 0:
                    return 0
                else:
                    print(f"{record}")
                    return count_student_records(record - 1, id)
        
        return "record do not exits"
print(count_student_records(2, "ST03",))
    
# print(count_student_records())
print("anser")





import functools

def track_calls(func):
    @functools.wraps(func)  # Keeps the original function's name and docstring
    def wrapper(*args, **kwargs):
        # 1 & 5. Increment the persistent counter across separate calls
        wrapper.calls += 1
        
        # 4. Print the current count clearly
        print(f"📢 [Decorator] '{func.__name__}' has been called {wrapper.calls} time(s).")
        
        # 2 & 3. Accept any args/kwargs and return the original function's result unchanged
        return func(*args, **kwargs)
    
    # 4. Initialize the counter as an attribute on the wrapper so it's accessible externally
    wrapper.calls = 0
    return wrapper


# Applying the decorator to analyze_records
@track_calls
def analyze_records(data_list):
    student_count = {}
    for student, activity in data_list:
        student_count[student] = student_count.get(student, 0) + 1
    return student_count

# --- Testing the Implementation ---

# Call 1
res1 = analyze_records(records)
print("Result 1:", res1)
print(f"External Counter Check: {analyze_records.calls}\n" + "-"*40)

# Call 2 (Demonstrating keyword arguments)
res2 = analyze_records(data_list=records)
print("Result 2:", res2)
print(f"External Counter Check: {analyze_records.calls}\n" + "-"*40)

