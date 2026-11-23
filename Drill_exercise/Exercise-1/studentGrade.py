def grade(grade_arr):

    name = grade_arr[0]

    grade = [int(x) for x in grade_arr[1:]]
    avg_total = sum(grade) / len(grade)

    if avg_total >= 70 and avg_total <= 100:
        return f"{name} - {avg_total} - Grade: A"
    elif avg_total < 70 and avg_total >= 60:
        return f"{name} -  {avg_total} - Grade: B"
    elif avg_total < 60 and avg_total >= 50:
        return f"{name} -  {avg_total} - Grade: C"
    elif avg_total < 50 and avg_total >= 45:
        return f"{name} -  {avg_toatal} - Grade: D"
    elif avg_total < 45 and avg_total >= 40:
        return f"{name} -  {avg_total} - Grade: E"
    else:
        return f"{name} -  {avg_toatal} - Grade: F"
        
# return {"average": avg_total, "result": f"{name} - {avg_total:.2f} - Grade: {letter}"}

print(grade(['mueez', 45, 67, 78, 90]))


def grade(grade_arr):

    name = grade_arr[0]

    grade = [int(x) for x in grade_arr[1:]]
    avg_total = sum(grade) / len(grade)

    if avg_total >= 70 and avg_total <= 10:
        Grade = "A"

    elif avg_total >= 60:
        Grade = "B"
    elif avg_total >= 50:
        Grade = "C"
    elif avg_total >= 45:
        Grade = "D"
    elif avg_total >= 40:
        Grade = "E"
    else:
        Grade = "F"

    return {"average": avg_total, "result": f"{name} - {avg_total:.2f} - Grade: {Grade}"}


student_data = [
    {"name": "Alice", "scores": [80, 90, 75]},
    {"name": "Bob", "scores": [60, 58, 62]},
    {"name": "Charlie", "scores": [95, 92, 88]},
    {"name": "David", "scores":[35, 0, 0]}
]

first_student_data = [student_data[0]["name"]] + student_data[0]["scores"]
first_grade_avg = grade(first_student_data)

highest = first_grade_avg
lowest = first_grade_avg

for student in student_data[1:]:
    each_student = [student["name"]] + student["scores"]
    grad_avg_each = grade(each_student)

    if grad_avg_each["average"] > first_grade_avg["average"]:
        highest = grad_avg_each

    if grad_avg_each["average"] < first_grade_avg["average"]:
        lowest = grad_avg_each

print("Highest:", highest["result"])
print("Lowest:", lowest["result"])




