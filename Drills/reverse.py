def reverse_string(value):
    str = ""
    val_len = len(value)
    for i in range(val_len - 1, -1, -1):
        str += value[i]
    return str
