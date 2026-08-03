#  Implement contact_lookup(contact, key). The contact argument is a dictionary. Return the value for the given key. If the key does not exist, return Not found.
 
# def contact_lookup(contact, key):
#     for each_key in contact.keys():
#         if contact[each_key] == key:
#             return contact[each_key]
#     return "Not found"
# print(contact_lookup({"age":22,"city":"Lagos","name":"Ada"},"Ada"))

def contact_lookup(contact, key):
    return contact.get(key, "Not found")
print(contact_lookup({"age":22,"city":"Lagos","name":"Ada"},"name"))


# banana
# Input: ["banana"]
# Expected: {"a":3,"b":1,"n":2}
# hello
# Input: ["hello"]
# Expected: {"e":1,"h":1,"l":2,"o":1}
def character_counter(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    # for char in text:
    #     if char in counts:
    #         counts[char] += 1
    #     else:
    #         counts[char] = 1
    return counts
print(character_counter("banana"))


# basic grouping
# Input: [["Ada","Halima","Adamu","Tunde"]]
# Expected: {"A":["Ada","Adamu"],"H":["Halima"],"T":["Tunde"]}
# case normalization
# Input: [["ada","Amina","bola"]]
# Expected: {"A":["ada","Amina"],"B":["bola"]}
def group_by_first_letter(names):
    the_grouping = {}
    for name in names:
        cleaned_name =  name.strip()
        if cleaned_name ==  "":
            continue 
        first_letter = cleaned_name[0].upper()
        
        if first_letter not in the_grouping:
            the_grouping[first_letter] = []
        the_grouping[first_letter].append(cleaned_name)
    return the_grouping

print(group_by_first_letter(["ada","Amina","bola"]))

# basic tags
# Input: [["Python","python"," AI ","ai"]]
# Expected: ["ai","python"]
# already unique
# Input: [["backend","frontend"]]
# Expected: ["backend","frontend"]
def unique_tags(tags):
    unique = []
    for item in tags:
        cleaned_tag = item.strip().lower()
        if cleaned_tag == "":
            continue
        unique.append(cleaned_tag)
    return sorted(set(unique))

print(unique_tags(["Python","python"," AI ","ai"]))


#number comparison
# Input: [[1,2,3],[2,3,4]]
# Expected: {"both":[2,3],"only_a":[1],"only_b":[4]}
# word comparison
# Input: [["python","ai"],["ai","data"]]
# Expected: {"both":["ai"],"only_a":["python"],"only_b":["data"]}
def set_comparison(a, b):
    a_and_b = list(set(a) & set(b))
    only_a = list(set(a) - set(b))
    only_b = list(set(b) - set(a))
    return {
        "both": a_and_b,
        "only_a": only_a,
        "only_b": only_b
    }

print(set_comparison([1,2,3],[2,3,4]))


# basic top scorer
# Input: [{"Ada":90,"Tunde":85,"Halima":95}]
# Expected: "Halima"
# single scorer
# Input: [{"Ada":70}]
def top_scorer(scores):
    res = 0
    list_val = []
    if len(scores) == 0:
        return "no score" 
    for val in scores.keys():
        if scores[val] > res:
            res = scores[val]
            list_val = [val]
        elif scores[val] == res:
            list_val.append(val)
    return sorted(list_val)[0]
print(top_scorer({"Ada":90,"Tunde":95,"Halima":95}))
    



    
