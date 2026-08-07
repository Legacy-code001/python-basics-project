def generate_remote():
    yield "channel"
    yield "Nta"


my_generator = generate_remote()
print(my_generator)
print(next(my_generator))


def febonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
    
my_fib = febonacci()

for f in febonacci():
    if f > 30:
        break
    print(f)


def infinite_coffee_stream():
    order_id = 1
    drinks = ['Latte', 'Mocha', 'Cappuccino']
    while True:
        # Cycle through the drinks list based on the order ID
        drink = drinks[order_id % len(drinks)]
        yield {
            'id': order_id,
            'drink': drink,
            'price': 4.50 + (order_id % 2) * 0.50
        }
        order_id += 1

# Process the first 3 orders from our infinite stream
stream = infinite_coffee_stream()
print(next(stream))  # Order 1
print(next(stream))  # Order 2
print(next(stream))  # Order 

# yield from
def morning_shift():
    yield "Espresso"
    yield "Latte"

def afternoon_shift():
    yield "Mocha"
    yield "Iced Coffee"

def full_day_menu():
    yield from morning_shift()    # Delegates directly to the sub-generator
    yield from afternoon_shift()  # Delegates directly to the sub-generator

for drink in full_day_menu():
    print("Serving:", drink)


# generator pipeline chaining
def order_source():
    # Simulate a database stream of raw orders
    yield {'id': 1, 'drink': 'latte', 'price': 4.50}
    yield {'id': 2, 'drink': 'mocha', 'price': 5.00}
    yield {'id': 3, 'drink': 'espresso', 'price': 3.50}

def apply_tax_pipeline(stream):
    # This generator modifies prices lazily as they pass through
    for order in stream:
        order['price_with_tax'] = order['price'] * 1.10
        yield order

def receipt_formatter(stream):
    # This generator formats the modified orders
    for order in stream:
        yield f"Order #{order['id']}: {order['drink'].capitalize()} — ₦{order['price_with_tax']:.2f}"

# Chain the generators together!
raw_orders = order_source()
taxed_orders = apply_tax_pipeline(raw_orders)
receipts = receipt_formatter(taxed_orders)

for receipt in receipts:
    print(receipt)



# What You Should Find / Be Able to Do Afterward
# Explain the syntactic difference between a list comprehension [x for x in range(10)] and a generator expression (x for x in range(10)).
# Write a single-line generator expression that generates squared prices for a list of coffee cups without using the yield keyword inside a function.
# Explain why generator expressions are preferred over list comprehensions when passing large datasets into aggregations like sum(), max(), or min().
