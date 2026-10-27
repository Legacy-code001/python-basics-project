
def conv_roman():
    standard_roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
    roman = input("roman value : ").upper()
    int_val = 0
    for val in roman:
        if val not in standard_roman:
            print("ivalid roman numeral")
            return
    
    for i in range(len(roman)):
            if i + 1 < len(roman) and standard_roman[roman[i]] < standard_roman[roman[i + 1]]:
                int_val -= standard_roman[roman[i]]
            else:
                int_val += standard_roman[roman[i]]
    return int_val
print(conv_roman())