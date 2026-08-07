def triangle_pattern(n):
    res = ""
    if n < 1:
        return ""
    for i in range(1, n+1):
        if i == n:
            res += ("*" * i) 
        else:
            res += ("*" * i) + "\n"
    return res

print(triangle_pattern(6))
