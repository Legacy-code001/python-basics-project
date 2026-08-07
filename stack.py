##deque as a stack

from collections import deque

stack = deque()

# use dir(stack) to method tat comes with deque all the me

s = []

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, data):
        self.container.append(data)
    def pop(self):
        if self.is_empty():
            raise indexError("the container is empty")
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def len(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container) == 0
    def reverse_str(self):
        return self.container.reverse()

    def reverse_str_2(val):
        stackVal = stack()
        for i in val:
            stackVal.append(i)
        str = ''
        while len(stackVal) != 0:
            str += stackVal.pop()
        return str

    def __str__(self):
        # Converts deque to a list for a readable display
        return f"Stack({list(self.container)})"



#         Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


def is_match(ch1, ch2):
    match_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    return match_dict[ch1] == ch2
    
def is_balanced(str):
    stackBal = Stack()
    for i in str:
        if i == "(" or i == "[" or i == "{":
            stackBal.push(i)
        elif i == ")" or i == "]" or i == "}":
            if stackBal.len() == 0:
                return False
            if not is_match(i, stackBal.pop()):
                return False

    return stackBal.len() == 0


"""second task """
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr

    if __name__ == '__main__':
        print(reverse_string("We will conquere COVI-19"))
        print(reverse_string("I am the king"))


s = Stack()
s.push("one")
s.push("2")
s.push("three")
s.push("4")
s.push("5")
print(s.is_empty())
print(s.peek())
s.pop()
print(s.len())
# print(s.__str__())
print(s.reverse_str())

print(s)
if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))