def balance_parentheses(input_val):
    counter = 0

    for char in input_val:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

        if counter < 0:
            return f"Output: Not Balanced"

    if counter == 0:
        return f"Output: Balanced"
    else:
        return f"Output: Not Balanced"


print(balance_parentheses("(a+b) * (c-d)")
)


    