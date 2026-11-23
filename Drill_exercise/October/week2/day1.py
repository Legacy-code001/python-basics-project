# Exercise 22: Singly Linked List Implementation
# Practice Problem: Create a basic Node class and a LinkedList class. Implement a method to append a new node to the end of the list and a method to display the list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedClass:
    def __init__():
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print("{cuurrent.data} -> ", end="")
            current = current.next
        print("None")













if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")






