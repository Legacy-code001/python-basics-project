# def chunk_list(items, size):
#     res = []
#     for i in range(0, len(items), size):
#         chunk = items[i: i + size]
#         res.append(chunk)
#     return res
# print(chunk_list(["a","b","c"], 2))

# def dedupe_preserve_order(items):
#     res = []

#     for val in items:
#         if val not in res:
#             res.append(val)
#     return res

def point_summary(point):
    x = ""
    y = ""
    x,y = point
    res = {
        x: int(x),
        y: int(y),
        "manhattan": x + y
    }
    return res
print(point_summary((5,8)))


# list comprehension
def clean_words(words):
    
    res = [x.strip().lower() for x in words if x.strip().lower() != ""]
    return res



