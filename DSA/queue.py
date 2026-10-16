
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        return self.buffer.appendleft(val)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("the container is empty")
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
    def __str__(self):
        # Converts deque to a list for a readable display
        return f"Queue({list(self.buffer)})"
    
    
dq = Queue()


dq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
dq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
dq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
},
)

# print(dq.size())
# print(dq.dequeue())
print(dq)
print(dq.size())
