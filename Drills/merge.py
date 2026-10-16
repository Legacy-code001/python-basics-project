# def merge_logs(log_a, log_b):
#     merge_res = []
#     i = j = 0

#     while i < len(log_a) and j < len(log_b):
#         if log_a[i] <= log_b[j]:
#             merge_res.append(log_a[i])
#             i+=1
#         else:
#             merge_res.append(log_b[j])
#             j+=1

#     merge_res.extend(log_a[i:])
#     merge_res.extend(log_b[j:])

#     return merge_res


# # three recruits three shifts
# # Input: [["Ada","Tunde","Halima"],3]
# # Expected: [["Ada","Tunde","Halima"],["Tunde","Halima","Ada"],["Halima","Ada","Tunde"]]
# # single shift
# # Input: [["Ada","Tunde"],1]
# # Expected: [["Ada","Tunde"]]

# def rotation_schedule(roster, shifts):
#     # Handle empty list edge case
#     if len(roster) == 0:
#         return []
        
#     schedule_history = []
    
#     # Loop from 0 up to shifts (inclusive) to capture all intermediate rotation lists
#     for i in range(shifts):
#         actual_shifts = i % len(roster)
        
#         # Slice the list from the shift point and join the pieces
#         rotated = roster[actual_shifts:] + roster[:actual_shifts]
        
#         # Append this variation layout to our master collection
#         schedule_history.append(rotated)
        
#     return schedule_history


# 1. Ada (15)\n2. Tunde (8)"
def exercise_scoreboard(records):
    # : Accumulate scores using a dictionary and .get()
    score_map = {}
    for name, score in records:
        score_map[name] = score_map.get(name, 0) + score
        
    # : Sort the recruits
    # Sort criteria: 1. Total score highest-to-lowest (-x[1])
    #                2. Name alphabetically lowest-to-highest (x[0])
    sorted_recruits = sorted(score_map.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the scoreboard lines
    scoreboard_lines = []
    for rank, (name, total_score) in enumerate(sorted_recruits, start=1):
        line = f"{rank}. {name} ({total_score})"
        scoreboard_lines.append(line)
        
    #  Join lines with newlines (no trailing newline)
    return "\n".join(scoreboard_lines)

print(exercise_scoreboard([["Ada",10],["Tunde",8],["Ada",5]]))

# drill-6
def validate_pass(pass_code):
    if pass_code == "":
        return "no pass"
    if len(pass_code) < 5:
        return "too short"
    if pass_code[0] == "p":
        return "invalid prefix"
    return "valid"
