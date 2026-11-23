"""
if n = 5
the stacks follows first enter(bottom) and last enters(top)
total(1) base case hit at n == 1,  and execution stops, 
total(2) execution pause and wait for total(1)
total(3) execution pause and wait for total(2)
total(4) execution pause and wait for total(3)
total(5) execution pause and wait for total(4)

the return values
start from the last enter
total(1) return 1 and leave the stack
total(2) return 2 + (2 - 1)
total(3) return 3 + (3 - 1)
total(4) return 5 + (5 - 1)
total(5) return 4 + (4 - 1)

"""