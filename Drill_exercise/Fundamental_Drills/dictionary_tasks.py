prices = [3.00, 4.00, 5.00]

price_comp = [x ** 2 for x in prices]
price_filter = [needs_p for needs_p in prices if needs_p >= 4.00]
print(price_filter)
print(price_comp)

stock = {"cups": 100, "lids": 150}

doubled_price = {utencils: price * 2 for utencils, price in stock.items()}
print(doubled_price)

raw_spices = {"  cinnamon ", "cocoa ", "cinnamon", "nutmeg"}
clean_spices = {}

clean_spices = {clean_ind.strip().lower() for clean_ind in raw_spices}
print(clean_spices)

messy_names = ["LATTE", "latte", "espresso", "latte"]

all_upper = {each.upper() for each in messy_names}
print(all_upper)

raw_data = [12, -5, 7, 4, -1, 0, 9]

# Front handles the even/odd logic | Back drops the negatives
processed = [x * 2 if x % 2 == 0 else x for x in raw_data if x >= 0]

print(processed)
# Output: [24, 7, 8, 0, 9]

scores = [65, 92, 78, 50, 95]

# Nesting the second 'if-else' inside the 'else' branch of the first
labels = ["Excel" if s >= 90 else "Pass" if s >= 70 else "Fail" for s in scores]

print(labels)
# Output: ['Fail', 'Excel', 'Pass', 'Fail', 'Excel']

# [item for item in iterable Filter]
[x for x in [1, 2, 3, 4] if x > 2]
# Output: [3, 4] (Length shrinks to 2)


scores = [65, 92, 78, 50, 95, -99, -64]

cond = [x * 2 if x >= 70 else x ** 2 if x >= 80  else x for x in scores if x >= 0]

print(cond)


matrix = [,
    [4, 5, 6]
]

# Goal: Turn columns into rows -> [[1, 4], [2, 5], [3, 6]]

transposed = [[row[i] for row in matrix] for i in range(3)]

print(transposed)
# Output: [[1, 4], [2, 5], [3, 6]]



If the button doesn't work, copy and paste this link into your browser:
http://localhost:8000/reset-password?token=5wS8dju6kbQYj6rF54WR0rwF8QHcvwJtpF0SC4dfxYw