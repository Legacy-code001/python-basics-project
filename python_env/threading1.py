from concurrent.futures import ThreadPoolExecutor
import time

def process_online_order(order_id):
    print(f"Processing order #{order_id}...")
    time.sleep(1.0) # Simulate waiting for the order to compile
    return f"Order #{order_id} ready!"

orders = [101, 102, 103, 104]

# Automate a pool of 4 workers
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks and collect futures
    futures = [executor.submit(process_online_order, o_id) for o_id in orders]
    
    # Retrieve results as they complete
    for future in futures:
        print(future.result())


