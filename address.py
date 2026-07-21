book = {}
book["malik"] = {"age": "24", "state":"oyo", "school":"poly"}
book["habeeb"] ={"age":"16", "state":"osun", "school":"lagacy"}
import json
s = json.dumps(book)
print(s)

# Use an 'r' before the string to make it a raw string
with open(r"C:\Users\owner\Desktop\book.txt", "w") as f:
    f.write(s)

f=open(r"C:\Users\owner\Desktop\book.txt", "r")

# # print(f.read())

s = f.read()

print(json.loads(s))

