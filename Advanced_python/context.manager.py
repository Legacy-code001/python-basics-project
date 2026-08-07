def make_latte():
    with EspressoMachine() as espresso_machine:
        with MilkSteamer() as milk_steamer:
            with Cup() as cup:
                espresso = espresso_machine.pull_shot()
                milk = milk_steamer.steam_milk()
                cup.fill(espresso)
                cup.add_milk(milk)
                return cup
    # All resources are AUTOMATICALLY cleaned up!

    # file operation usage
    # Reading files
with open('orders.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed!

# Writing files
with open('receipt.txt', 'w') as file:
    file.write("Order #101: Latte")
# File is automatically closed and saved!

# Multiple files
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.upper())

# 2. threading lock
import threading

lock = threading.Lock()

def process_order(order_id):
    with lock:  # Automatically acquires and releases lock
        print(f"Processing order #{order_id}")
        # Critical section
    # Lock is automatically released!


#3 Database connection, still acessing the files
import sqlite3

with sqlite3.connect('coffee.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()
# Connection is automatically closed!

# 4 temporary file usage
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Coffee order data')
    temp.seek(0)
    data = temp.read()
# Temp file is automatically deleted!

# 5 supressing exception
from contextlib import suppress

with suppress(FileNotFoundError):
    # This file might not exist
    with open('missing.txt') as f:
        data = f.read()
    # No exception is raised if file is missing!

# context manager with a class:
class CoffeeMachine:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type
        print(f"⏳ Preparing {coffee_type} machine...")
    
    def __enter__(self):
        print(f"✅ {self.coffee_type} machine ready!")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"🧹 Cleaning {self.coffee_type} machine...")
        if exc_type:
            print(f"⚠️ Error occurred: {exc_val}")
        print("✅ Machine cleaned!")
        # Returning False re-raises exceptions, True suppresses them
        return False
    
    def make_coffee(self):
        print(f"☕ Making {self.coffee_type}...")
        time.sleep(0.5)
        return f"Here's your {self.coffee_type}!"

# Usage
with CoffeeMachine("Latte") as machine:
    result = machine.make_coffee()
    print(result)


# ⏳ Preparing Latte machine...
# ✅ Latte machine ready!
# ☕ Making Latte...
# Here's your Latte!
# 🧹 Cleaning Latte machine...
# ✅ Machine cleaned!

# 2. Time handle usage
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"⏱️ Time: {elapsed:.4f} seconds")
        return False
    
    def elapsed(self):
        return time.time() - self.start

# Usage
with Timer() as timer:
    time.sleep(0.3)
    print(f"Elapsed: {timer.elapsed():.4f}s")



# 4 temporary file cleanup
import os
import tempfile

class TemporaryFile:
    def __enter__(self):
        self.path = tempfile.mktemp()
        self.file = open(self.path, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.path)
        print(f"✅ Deleted {self.path}")
        return False

# Usage
with TemporaryFile() as f:
    f.write("Coffee data")
    f.seek(0)
    print(f.read())
# File is automatically deleted!

class Counter:
    def __enter__(self):
        self.count = 0
        return self
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        print(f"operation:{self.count}")
        return False
    
    def increament(self):
        self.count += 1
    
with Counter() as counter:
    counter.increament()
    counter.increament()
    counter.increament()

''' The contextlib.contextmanager Approach:'''
from contextlib import contextmanager
@contextmanager
def coffee_machine(coffee_type):
    print(f"⏳ Preparing {coffee_type} machine...")
    print(f"✅ {coffee_type} machine ready!")
    try:
        yield f"Machine for {coffee_type}"  # Resource is yielded
    finally:
        print(f"🧹 Cleaning {coffee_type} machine...")
        print("✅ Machine cleaned!")

# Usage
# with coffee_machine("Latte") as machine:
#     print(f"☕ Making coffee with {machine}")

# ⏳ Preparing Latte machine...
# ✅ Latte machine ready!
# ☕ Making coffee with Machine for Latte
# 🧹 Cleaning Latte machine...
# ✅ Machine cleaned!

''' contextlib manager as decorator -1 '''


from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"⏱️ Took {elapsed:.4f}s")

# Usage
with timer():
    time.sleep(0.3)
# Output: ⏱️ Took 0.3002s

''' file with context behaviour: -2'''
@contextmanager
def managed_file(filename, mode='r'):
    f = open(filename, mode)
    print(f"📂 Opening {filename}")
    try:
        yield f
    finally:
        print(f"📂 Closing {filename}")
        f.close()

# Usage
with managed_file('orders.txt', 'w') as f:
    f.write("Latte\nMocha\nCappuccino")

# 📂 Opening orders.txt
# 📂 Closing orders.txt

''' redirecting output -4'''

import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def capture_output():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

# Usage
with capture_output() as output:
    print("This goes to the capture")
    print("So does this")
    captured = output.getvalue()
    print(f"📄 Captured:\n{captured}")


''' context manager with argument 1 '''

@contextmanager
def brew_coffee(drink_type, extra_shot=False):
    print(f"⏳ Brewing {drink_type}...")
    if extra_shot:
        print("☕ Adding extra shot")
    try:
        yield f"{drink_type} with{' extra shot' if extra_shot else ''}"
    finally:
        print(f"🧹 Cleaning {drink_type} machine...")

# Usage
with brew_coffee("Latte", extra_shot=True) as drink:
    print(f"☕ Ready: {drink}")


# ⏳ Brewing Latte...
# ☕ Adding extra shot
# ☕ Ready: Latte with extra shot
# 🧹 Cleaning Latte machine...

'''nexted loop manager: 2'''
@contextmanager
def espresso_machine():
    print("⚡ Starting espresso machine")
    yield "Espresso"
    print("⚡ Stopping espresso machine")

@contextmanager
def milk_steamer():
    print("🥛 Heating milk steamer")
    yield "Milk"
    print("🥛 Cooling milk steamer")

@contextmanager
def make_latte():
    with espresso_machine() as espresso:
        with milk_steamer() as milk:
            yield f"{espresso} + {milk} = Latte"

# Usage
with make_latte() as result:
    print(f"☕ {result}")

# ⚡ Starting espresso machine
# 🥛 Heating milk steamer
# ☕ Espresso + Milk = Latte
# 🥛 Cooling milk steamer
# ⚡ Stopping espresso machine

 '''context manager with handling exception'''
@contextmanager
def handle_errors():
    try:
        yield
    except ValueError as e:
        print(f"❌ Value error: {e}")
    except TypeError as e:
        print(f"❌ Type error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise

# Usage
with handle_errors():
    x = int("not a number")  # ValueError caught!

with handle_errors():
    x = [1, 2, 3]
    y = x + 5  # TypeError caught!

print("✅ Program continues")


''' reuseable context manager'''