from collections import deque
import time
import threading

class ManualFoodOrderingSystem:

    def __init__(self):
        self.order_queue = deque()
        # What it explicitly does in your systemWithout a lock, Python's memory management can glitch if one thread tries to append an item while another thread is simultaneously popping an item. The lock acts like a bathroom key: only one thread can hold it at a time.
        self.order_lock = threading.Lock()
        self.order_available = ['pizza','samosa','pasta','biryani','burger']
        # self.order_running = True
        self.all_order_placed = False

    def place_order(self):
        for item in self.order_available:
            #3
            with self.order_lock:
                self.order_queue.appendleft(item)
            print(f"[placed] {item}\n")

        time.sleep(0.5)
        self.all_order_placed = True
            # 2
            # print("type your order and click enter, click exit when your are done")
            # input_order = input("The order: ").strip()
            # if input_order.lower() == "exit":
                # self.order_running = False
                # break
    def serve_order(self):
        while  not self.all_order_placed or len(self.order_queue) > 0:
            order = None
            with self.order_lock:
                if len(self.order_queue) > 0:
                    order = self.order_queue.pop()
            if order:
                print(f"\n  [Served] {order}")
                # end="": Overrides the default behavior of print(), which normally adds a newline (\n) at the end. This keeps the cursor on the exact same line.
                # flush=True: Forces Python to display the text on the screen immediately. Normally, Python buffers (holds) text output until a newline character is printed.
                print("Done, Next...")
            time.sleep(2.0)


if __name__ == "__main__":
    system = ManualFoodOrderingSystem()

    # 1. Create threads
    producer_thread = threading.Thread(target=system.place_order)
    consumer_thread = threading.Thread(target=system.serve_order)

    # 2. Start the user input thread
    producer_thread.start()
    # print(producer_thread.start())

    # 3. Wait 1 second before starting the background serving thread
    time.sleep(1.0)
    consumer_thread.start()
    # print(consumer_thread.start())

    # Join threads to ensure clean shutdown when user types 'exit'
    producer_thread.join()
    consumer_thread.join()
    # print("System shut down completely.")

    t = time.time()

print("done in : ",time.time()-t)
print("Hah... I am completed all the order")
# dq.place_order("pizza")
# dq.place_order("samosa1")
# dq.place_order("samosa3")
# dq.place_order("samosa5")
# dq.place_order("samosa7")
# print(dq.serve_order())
# print(dq.serve_order())
# print(dq)

# print(dq.is_empty())
# 'pizza','samosa','pasta','biryani','burger'


"""another methods"""



class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()