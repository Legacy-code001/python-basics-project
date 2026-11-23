avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']

count = 0

for i in range(len(avengers)):
    count += 1
print(count)

# avengers.append("spider-man")
# print(avengers)
# index = avengers.index("Captain America")
# val = avengers.pop(index)
# avengers[0] = val
# print(avengers)

avengers[0] = 'Captain America'
avengers[1] = 'Iron Man'
print(avengers)

avengers[2] = 'Hulk'
avengers[3] = 'Black Window'

scores = [92, 85, 76, 58, 89, 91, 73, 84]
Grade = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for grad, score in zip(Grade, scores):


# count = 0
# for i in range(len(scores)):
#     if scores[i] >= 90 and scores[i] <= 100:
#         print(f"A: {scores[i]}")
#         count+=1
#         print(f"A: {count} student ")
#     elif scores[i] >= 80 and scores[i] <= 89:
#         count = 0
#         print(f"B: {scores[i]}")
#         count += 1
#         print(f"A: {count} student ")
#     else:
#         print('not in range')
