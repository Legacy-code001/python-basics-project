import json
json_string = '''
{
    "name": "Maulik",
    "age": 30,
    "is_employee": true,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    }
}
'''




# json.load()
# Reads JSON from a file

# json.loads()
# Converts a JSON string into a Python object

# # JSON string
# json_string = '''
# {
#     "name": "Maulik",
#     "age": 30,
#     "is_employee": true,
#     "skills": ["Python", "Data Analysis", "Machine Learning"],
#     "address": {
#         "street": "123 Main St",
#         "city": "Wonderland"
#     }
# }
# '''

# json.loads()
# Converts a JSON string into a Python object
record1 = json.loads(json_string)
print(record1)
print(type(record1))


# json.dumps()
# Converts a Python object into a JSON string
string_record = json.dumps(record1)
print(string_record)
print(type(string_record))


# json.load()
# Reads JSON from a file

# json.dump() writes Python dict data directly into a file.
with open("record1.json", "w") as file:
    json.dump(record1, file, indent=4)

with open("record1.json", "r") as file:
    product = json.load(file)
print(f"read json file to return a dictionary obj: {product}")
print(product['skills'][1])

"""error handling"""

json_string2 = '''
{
    "name": "Krishna",
    "age": 30
    "is_employee": true
}
'''

try:
    dict_string = json.loads(json_string2)
    print(f"our second dict: {dict_string}")
except json.JSONDecodeError as e:
    print(f"failed to parse json: {e}")
