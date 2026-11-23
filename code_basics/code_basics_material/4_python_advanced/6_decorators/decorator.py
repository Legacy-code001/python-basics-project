import time

def timer(func):
    def wrapper(*args, **kwags):
        start = time.time()
        results = func(*args, **kwags)
        end = time.time()
        print(f"the time used by this funct: {func.__name__} is {(end - start *1000)} seconds")
        return results
    return wrapper

@timer
def squareNum(the_list):
    result1 = [x**2 for x in the_list]
    return result1
@timer
def cubeNum(the_list):
    result2 = [x**3 for x in the_list]
    return result2

print(squareNum([1, 2, 3, 4, 5]))
print(cubeNum([1, 2, 3, 4, 5]))

