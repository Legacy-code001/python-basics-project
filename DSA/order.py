from collections import deque
import time
import threading

class ManualFoodOrderingSystem:
    def __init__(self):
        self.order_queue = deque()
        self.order_lock = threading.Lock()
        self.order_running = True

    def place_order(self):
        while self.order_running:
            print("type your order and click enter, click exit when your are done")

            input_order = input("The order: ").strip()
            if input_order.lower() == "exit":
                self.order_running = False
                break
            if user_order:
                with self.order_lock:
                    self.order_queue.appendleft(input_order)
            print(f"[placed] {input_order}\n")
    
    def serve_order(self):
        while self.order_running:
            order = None
            with self.order_lock:
                if len(input_order) > 0:
                    self.order_queue.pop()
            if order:
                print(f"\n  [Served] {order}")
                if self.running:
                    print("Enter order: ", end="", flush=True)

            time.sleep(2.0)


if __name__ == "__main__":
    system = ManualFoodOrderingSystem()

    # 1. Create threads
    producer_thread = threading.Thread(target=system.place_order)
    consumer_thread = threading.Thread(target=system.serve_order)

    # 2. Start the user input thread
    producer_thread.start()

    # 3. Wait 1 second before starting the background serving thread
    time.sleep(1.0)
    consumer_thread.start()

    # Join threads to ensure clean shutdown when user types 'exit'
    producer_thread.join()
    consumer_thread.join()
    print("System shut down completely.")

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
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