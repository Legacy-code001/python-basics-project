from collections import  deque

# class Binary:
#     def __init__(self, start=1, end = 10):
#         self.queue_list = deque()
#         self.binary_list = end
#         self.start = start

#     def binary(self):
#         for i in range(self.start, self.binary_list + 1):
#             result = bin(i)[2:]
#             self.queue_list.appendleft(result)
#         print(f"{list(self.queue_list)}")

# s = Binary()
# s.binary()


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

    def front(self):
        return self.buffer[-1]


def process_binary(n):
    numbers_bin = Queue()
    numbers_bin.enqueue("1")
    
    for n in range(10):
        front = numbers_bin.front()
        print(" ", front)
        numbers_bin.enqueue(front + '0')
        numbers_bin.enqueue(front + "1")
        numbers_bin.dequeue()

if __name__ == "__main__":
    process_binary(10)


# textInitial Queue: ["1"]

# Iteration 1: 
#   - Peek front: "1" -> Print "1"
#   - Enqueue "1" + "0" -> "10"
#   - Enqueue "1" + "1" -> "11"
#   - Dequeue "1"
# Queue becomes: ["10", "11"]

# Iteration 2: 
#   - Peek front: "10" -> Print "10"
#   - Enqueue "10" + "0" -> "100"
#   - Enqueue "10" + "1" -> "101"
#   - Dequeue "10"
# Queue becomes: ["11", "100", "101"]