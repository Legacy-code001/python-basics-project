def fib_sequence():
    the_check = input("Input the number: ")


    sequence = [0, 1]
    total = 0
    if the_check.isdigit():
        the_int_val = int(the_check)
        if the_int_val <= 0:
            return []
        elif the_int_val == 1:
            return [0]
        the_int_val = int(the_check)
        for i in range(2, the_int_val):
            val = sequence[-1] + sequence[-2]
            sequence.append(val)

    for i in range (len(sequence)):
        if sequence[i]%2 == 0:
            total += sequence[i]
    return f"the sequence{sequence } and  Even Sum: {total}"

print(fib_sequence())

def fib_sequence():
    the_check = input("Input the number: ")

    
    if the_check.isdigit():
        the_int_val = int(the_check)

        if the_int_val <= 0:
            return
        elif the_int_val == 1:
            print(the_int_val)
            return

        a, b = 0, 1
        for _ in range(2, the_int_val):
            a, b = b, b + a

        for _ in range(the_int_val):
            print(b, end=" ")

            a, b = b - a, a

        print()
fib_sequence()
