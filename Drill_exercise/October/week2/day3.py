num = [1,2,3,4,5,6,7,8]


squre_even = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num)))
print(squre_even)

# time.perf_counter() returns a high-resolution float value in seconds from a monotonic clock, making it the best tool in Python for measuring how long code takes to run.

import time

def timer(func):
    def wrapper(*args, **kwags):
        start = time.time()
        results = func(*args, **kwags)
        end = time.time()
        print(end - start)
        return results 
    return wrapper
        


@timer
def sleep():
    print("starting the process")
    time.sleep(2)
    print("ending the processing")

sleep()