def binary_search_recursive(arr, low, high, x):
    # Base Case: target is not in the list
    if high < low:
        return -1

    mid = (low + high) // 2

    # If element is at the middle
    if arr[mid] == x:
        return mid
    
    # If element is smaller than mid, search left sub-array
    elif arr[mid] > x:
        return binary_search_recursive(arr, low, mid - 1, x)
    
    # If element is larger than mid, search right sub-array
    else:
        return binary_search_recursive(arr, mid + 1, high, x)

data = [10, 20, 30, 40, 50, 60]
target = 50
result = binary_search_recursive(data, 0, len(data) - 1, target)

print(f"Target found at index: {result}")

employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]

employ_des = [sorted(employees, key=lambda x: x[2], reverse=True)]
print(employ_des)

def finabocci_generator():
    a,b = 0, 1

    while True:
        yield a
        a, b = b , a + b

finbab = finabocci_generator()

for f in finbab:
    if f < 8:
        print(f)
 
#  or

def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator
fib = fibonacci_gen(8)

print("First 8 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")