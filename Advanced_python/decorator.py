# decorator with timer
import time

def timed(func):
    def wrapper(*arg, **wrag):
        start = time.time()
        results = func(*arg, **wrag)
        end = time.time()
        print(func.__name__ +" took " + str((end - start) * 100) + "mil sec")
        return results
    return wrapper
@timed
def square_num(numbers):
    results = []
    for num in numbers:
        results.append(num * num)
    return results
@timed
def cube_num(numbers):
    results = []
    for num in numbers:
        results.append(num * num * num)
    return results

array = range(1, 100)
the_square = square_num(array)

array = range(1, 100)
the_cube = cube_num(array)


# taking function as argument

def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"

def shout(speaker, name):
    return speaker(name).upper()

print(shout(say_hello, "Bob"))   # Output: HELLO, BOB!
print(shout(say_goodbye, "Bob")) # Output: GOODBYE, BOB!


# The upgrade kit (decorator)
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Use the original machine
        elapsed = time.time() - start
        print(f"⏱️ Took {elapsed:.2f}s")
        return result
    return wrapper

# Apply the upgrade
@time_it
def make_coffee(drink_type):
    print(f"Making {drink_type}...")
    return f"Here's your {drink_type}!"

# Use the upgraded machine
make_coffee("Latte")


# validation decorator
def validate_order(func):
    def wrapper(order_id, drink, price):
        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError(f"Invalid order_id: {order_id}")
        if not drink or not isinstance(drink, str):
            raise ValueError(f"Invalid drink: {drink}")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError(f"Invalid price: {price}")
        return func(order_id, drink, price)
    return wrapper

@validate_order
def process_order(order_id, drink, price):
    print(f"Processing: #{order_id} - {drink} (₦{price:.2f})")
    return "Processed!"

# Works fine
process_order(101, "Latte", 4.50)

# Raises error
try:
    process_order(-1, "Mocha", 5.00)
except ValueError as e:
    print(f"Error: {e}")

# retry decorator
def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    print(f"⚠️ Attempt {attempts} failed. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_api_call():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("API call failed!")
    return "Success!"


# to preserve metadata
from functools import wraps

def proper_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@proper_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"

print(greet.__name__)   # Output: greet (preserved!)
print(greet.__doc__)    # Output: Greet someone. (preserved!)

# passing argument to decorator

def repeat(n):
    """Decorator that repeats a function n times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                print(f"Execution {i+1}/{n}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def make_coffee(drink_type):
    print(f"Making {drink_type}...")
    return f"☕ {drink_type}"

# Runs the function 3 times
results = make_coffee("Latte")
print(results)