# class StackCardboardCup:
#     def __init__(self, owner):
#         self.owner = owner

# class CupStack:
#     def __init__(self):

#         # The internal list used to hold our cups
#         self._cups = []
        
#     def push(self, cup):
#         self._cups.append(cup)  # Push to the top of the stack
        
#     def pop(self):
#         # Safety check: do not pop if the stack is empty!
#         if self.is_empty():
#             print("Action Blocked: The stack is empty!")
#             return None
#         return self._cups.pop()  # Pop from the top of the stack
        
#     def is_empty(self):
#         return len(self._cups) == 0
#     def __str__(self):
#         # Converts deque to a list for a readable display
#         return f"Queue({list(self._cups)})"

class CupQueue:
    def __init__(self):
        self._cups = []
        
    def enqueue(self, cup):
        self._cups.append(cup)  # Add to the back of the line
        
    def dequeue(self):
        if self.is_empty():
            print("Action Blocked: The conveyor chute is empty!")
            return None
        return self._cups.pop(0)  # Remove from the front of the line (Index 0)
        
    def is_empty(self):
        return len(self._cups) == 0
    def __str__(self):
        # Converts deque to a list for a readable display
        return f"Queue({list(self._cups)})"

cup_samp = CupQueue()
cup_samp.enqueue("coke")
cup_samp.enqueue("fanta")
cup_samp.enqueue("pepsi")
cup_samp.dequeue()
print(cup_samp)