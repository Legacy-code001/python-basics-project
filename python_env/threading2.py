# A web server handling multiple checkout requests concurrently
from concurrent.futures import ThreadPoolExecutor
import requests

def process_checkout_transaction(checkout_payload):
    # This involves slow network I/O calls to credit card gateways
    response = requests.post("https://gateway.com/charge", json=checkout_payload)
    return response.json()

# The server can handle 20 checkouts at once using a thread pool
with ThreadPoolExecutor(max_workers=20) as web_workers:
    web_workers.map(process_checkout_transaction, incoming_requests)



# submit()

# The Power of .submit(): Because it gives you a Future object, you can cancel tasks before they start (f.cancel()), check if they are done (f.done()), or attach callback routines
from concurrent.futures import ThreadPoolExecutor, as_completed

def square(n):
    return n * n

inputs = [1, 2, 3, 4]

with ThreadPoolExecutor() as executor:
    # You must manually submit tasks and keep track of the "Future" objects
    futures = [executor.submit(square, x) for x in inputs]
    
    # Process results instantly as they finish using as_completed
    for f in as_completed(futures):
        print(f.result())  # Order will be random/unpredictable



# map()
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

inputs = [1, 2, 3, 4]

with ThreadPoolExecutor() as executor:
    # Launches 4 threads; returns an iterator of results
    results = executor.map(square, inputs)
    
    # Order is guaranteed: [1, 4, 9, 16]
    for r in results:
        print(r)
