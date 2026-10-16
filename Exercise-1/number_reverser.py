def reverse_num(num):
    sign = -1 if num < 0 else 1

    num = abs(num)

    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = (reverse * 10) + digit
        num //=10

    return reverse * sign

print(reverse_num(567))