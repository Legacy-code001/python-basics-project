
"""
You will be given a dataset containing product details, and your goal is to extract and display the distinct product categories present in the inventory.

**Expected Output**


Unique Product Categories:

- Electronics
- Apparel
- Home Appliances
- Literatureure
"""

products = [
    {"product_name": "Laptop", "category": "Electronics", "price": 1200},
    {"product_name": "Jeans", "category": "Apparel", "price": 40},
    {"product_name": "Coffee Maker", "category": "Home Appliances", "price": 80},
    {"product_name": "Smartphone", "category": "Electronics", "price": 999},
    {"product_name": "Jacket", "category": "Apparel", "price": 60},
    {"product_name": "Blender", "category": "Home Appliances", "price": 150},
    {"product_name": "Book", "category": "Literature", "price": 15}
]

product_categories = {product["category"] for product in products}
print(product_categories)

### Task 2: Audience Analysis for Music Festival Organizer

"""
Your task is to help analyze the data and:

1. Identify unique attendees for each concert.
2. Find common attendees across the concerts.

The attendee data is provided in the next cell. Use set operations to complete the analysis and print a summary of the results.

**Expected Output:**

Unique Attendees for Each Concert:
- Concert A Only: {'Charlie'}
- Concert B Only: {'Eve'}
- Concert C Only: {'George', 'Elle'}

Common Attendees Between All Concerts: {'Bob'}
"""

concert_a_attendees = {"Alice", "Bob", "Charlie", "Diana"}
concert_b_attendees = {"Bob", "Diana", "Eve", "Frank"}
concert_c_attendees = {"Alice", "George", "Elle", "Frank","Bob"}

concert_a = {a for a in concert_a_attendees if a not in concert_b_attendees and a not in concert_c_attendees }

concert_b = {b for b in concert_b_attendees if b not in concert_a_attendees and b not in concert_c_attendees}

concert_c = {c for c in concert_c_attendees if c not in concert_a_attendees and c not in concert_b_attendees}

print(concert_a, concert_b, concert_c)

common_attendes = {a for a in concert_a_attendees if a in concert_b_attendees and a in concert_c_attendees }
print(common_attendes)

### Task 3: Temperature Trend Analysis

"""Your responsibility is to analyze this dataset and extract the records where the maximum temperature was above 70°F. 

Display the filtered temperatures.

The temperature data is given in the next cell."""

daily_temperatures = [68, 71, 74, 69, 70, 71, 68, 73, 72, 71, 70, 74, 72, 68]

filter_70s = [temp_70 for temp_70 in daily_temperatures if temp_70 >= 70]
print(filter_70s)

# unique temperature:
unique_temp = {unq_temp for unq_temp in daily_temperatures}
print(unique_temp)

dict_count = {temp: daily_temperatures.count(temp)  for temp in daily_temperatures}
print(dict_count)


### Task 6: Social Media Engagement Analysis

# You are tasked with helping a client analyze their social media data to identify trending hashtags and measure user engagement. Specifically, you need to extract posts that have received more than 100 likes. Your task is to filter these posts and store them in a variable called popular_posts.

posts = [
    {"content": "Loving the sunny weather today! #sunny #happy", "likes": 120},
    {"content": "Nothing beats a beach day. #beachday #sunny", "likes": 350},
    {"content": "A rainy day at home. #rainy #lazyday", "likes": 75},
    {"content": "Best coffee in town. #coffeelove #morning", "likes": 180},
    {"content": "Can't wait for the weekend. #weekend #party", "likes": 90}
]

popular_posts = [post["content"]for post in posts if post["likes"] > 100]
print(popular_posts)



popular_hastag = set(tag for post in popular_posts for tag in post.split() if tag.startswith('#'))
print(popular_hastag)

hastags= [tag for post in popular_posts for tag in post.split() if tag.startswith('#')]

count_hastag = {hash: hastags.count(hash) for hash in hastags}
print(count_hastag)

# popular_comment = [set(tag for post in popular_posts for tag in post.split() if tag.startswith('#'))]


# # Extract unique hashtags from popular posts using set comprehension
# hashtags = set(tag for post in popular_posts for tag in post.split() if tag.startswith('#'))
# hashtags

