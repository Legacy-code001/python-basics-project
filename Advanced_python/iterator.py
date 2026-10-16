# class RemoteControl():
#     def __init__(self):
#         self.channel = ["bcos", "osbc", "nta", "channel_tv", "arise_tv"]
#         self.index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.channel):
#             raise StopIteration
#         return self.channel[self.index]

# my_remote = RemoteControl()
# iter = iter(my_remote)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))


# # file are iterable
# with open('orders.txt', 'w') as f:
#     f.write("Latte\nMocha\nCappuccino")

# with open('orders.txt', 'r') as f:
#     # File objects are iterators themselves!
#     print(next(f).strip())  # Latte
#     print(next(f).strip())  # Mocha
#     print(next(f).strip())  # Cappuccino


# iterator with custom logic
class OrderProcessor:
    """An iterator that processes orders with custom logic."""
    
    def __init__(self, raw_orders):
        self.raw_orders = raw_orders
        self.index = 0
        self.processed_count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.raw_orders):
            raise StopIteration
            
        # Get the raw order
        raw = self.raw_orders[self.index]

        # Process the order (capitalize, add prefix)
        processed = f"CONFERENCE: {raw.upper()}"

         # Track statistics
        self.processed_count += 1
        
        self.index += 1
    
        return processed
        
    def get_stats(self):
        return {
            'total_processed': self.processed_count,
            'remaining': len(self.raw_orders) - self.index
        }

# Usage
raw_orders = ['latte', 'mocha', 'cappuccino', 'americano']
processor = OrderProcessor(raw_orders)

for order in processor:
    print(order)
    
print(processor.get_stats())  # {'total_processed': 4, 'remaining': 0}


# lazy evaluation in pythom

# EAGER evaluation: Computes all 1 million squares immediately in memory
def eager_squares(n):
    return [i**2 for i in range(n)]

# LAZY evaluation: Computes nothing upfront. Yields squares one by one.
def lazy_squares(n):
    for i in range(n):
        yield i**2

# Testing the lazy evaluation
generator = lazy_squares(1000000000) # Takes 0 seconds! No memory used yet.
print(next(generator))  # Output: 0 (Computes just the first one)
print(next(generator))  # Output: 1 (Computes just the second one)

# Eager list comprehension (Heavy memory usage)
eager_list = [x * 2 for x in range(1000000)]

# Lazy generator expression (Virtually 0 memory usage)
lazy_gen = (x * 2 for x in range(1000000))

print(next(lazy_gen))  # Output: 0


# iterators

class CountUpIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0  # State is stored as an object attribute

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# generators

def count_up_generator(limit):
    current = 0
    while current < limit:
        yield current  # Python automatically pauses and saves 'current'
        current += 1

# itertools

# islice(iterable, start, stop, step): Slices an iterator just like string slicing ([start:stop]), but safely works on lazy streams or files without copyinzg them into memory.

print(list(itertools.accumulate([1, 2, 3, 4])))  # Output: [1, 3, 6, 10]

data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# Output: # lazy evaluation in pythom

# EAGER evaluation: Computes all 1 million squares immediately in memory
def eager_squares(n):
    return [i**2 for i in range(n)]

# LAZY evaluation: Computes nothing upfront. Yields squares one by one.
def lazy_squares(n):
    for i in range(n):
        yield i**2

# Testing the lazy evaluation
generator = lazy_squares(1000000000) # Takes 0 seconds! No memory used yet.
print(next(generator))  # Output: 0 (Computes just the first one)
print(next(generator))  # Output: 1 (Computes just the second one)

# Eager list comprehension (Heavy memory usage)
eager_list = [x * 2 for x in range(1000000)]

# Lazy generator expression (Virtually 0 memory usage)
lazy_gen = (x * 2 for x in range(1000000))

print(next(lazy_gen))  # Output: 0


# iterators

class CountUpIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0  # State is stored as an object attribute

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# generators

def count_up_generator(limit):
    current = 0
    while current < limit:
        yield current  # Python automatically pauses and saves 'current'
        current += 1

# itertools

# islice(iterable, start, stop, step): Slices an iterator just like string slicing ([start:stop]), but safely works on lazy streams or files without copyinzg them into memory.

print(list(itertools.accumulate([1, 2, 3, 4])))  # Output: [1, 3, 6, 10]

data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# Output: 
# fruit [('fruit', 'apple'), ('fruit', 'banana')]
# vegetable [('vegetable', 'carrot')]


# chain(*iterables): Glues multiple distinct collections together into one smooth sequence.
letters = ['a', 'b']
numbers = [1, 2]
print(list(itertools.chain(letters, numbers)))  # Output: ['a', 'b', 1, 2]

# fruit [('fruit', 'apple'), ('fruit', 'banana')]
# vegetable [('vegetable', 'carrot')]


# chain(*iterables): Glues multiple distinct collection  together into one smooth sequence.
letters = ['a', 'b']
numbers = [1, 2]
print(list(itertools.chain(letters, numbers)))  # Output: ['a', 'b', 1, 2]
