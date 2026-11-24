# Exercise 23: Stack Implementation (LIFO)
# Practice Problem: Implement a Stack data structure using a Python list. Create methods for push (add), pop (remove), and peek (view top element).

website = []

website.append("google.com")
website.append("pynative.com")
website.pop(0)

print(website)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

browser_history = Stack()
browser_history.push("google.com")
browser_history.push("pynative.com")

print(f"Current Top: {browser_history.peek()}")
print(f"Popped: {browser_history.pop()}")
print(f"New Top: {browser_history.peek()}")


# Exercise 24: Queue Implementation (FIFO)
# Practice Problem: Implement a Queue data structure using collections.deque. Create methods for enqueue (add to back) and dequeue (remove from front).

from collection import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.append(self.item)
    def dequeue(self):
        if len(self.buffer) == 0:
            return "buffer collection is empty"
        self.buffer.popleft()
            
    def peek(self):
        return self.buffer[0] if self.buffer is not None else None


ticket_line = Queue()

ticket_line.enqueue("Customer A")
ticket_line.enqueue("Customer B")
print(f"Serving: {ticket_line.dequeue()}")
print(f"Next in line: {ticket_line.peek()}")