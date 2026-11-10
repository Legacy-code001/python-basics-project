fruit = 5,
vegitable = 3

About_me = f"i eat {fruit} fruit and {vegitable} vegitable daily"

"""
Create a variable and store the string “The Himalayas are one of the youngest mountain ranges on the planet.”

Print ‘The Himalayas’ using slice operator
Print “mountain range” using a negative index
Print “The Himalayas on the planet” using slice as well as f-string
"""

statement = 'The Himalayas are one of the youngest mountain ranges on the planet.'
print(statement[0:14])
print(statement[-30 : -16])



"""
You have created a string variable called string= ”There are 9 planets in the solar system”. After some time, you have realized that your sentence is incorrect and there are only 8 planets, now correct your sentence by replacing the incorrect words. (Bonus: Try to do it in one line)
"""

string = 'There are 9 planets in the solar system'

arry = string.split(' ')
arry[2] = "8"
new_str = " ".join(arry)
print(new_str)

print(" ".join(string.split(' ')[:2] + ["8"] + string.split(' ')[3: ]))
print(string.replace('9', '8'))