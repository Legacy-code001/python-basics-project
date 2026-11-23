def encryp_or_decrpt(shift, value , mode="encrypt"):
    result = ""

    if mode == "decrypt":
        shift = -shift
    
    for val in value:
        if val.isupper():
            result += chr((ord(val) + shift - 65) % 26 + 65)
        elif val.islower():
            result += chr((ord(val) + shift - 97) % 26 + 97)
        else:
            result += val
    
    return result

print(encryp_or_decrpt(1, "hello"))