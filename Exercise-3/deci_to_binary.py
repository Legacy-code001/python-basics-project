def deci_convert():
    the_deci_number = input("input the number: ")

    if the_deci_number.isdigit():
        the_int_val = int(the_deci_number)

        if the_int_val == 0:
            return "0"

        binary_str = ""

        while the_int_val > 0:
            remainder = the_int_val % 2 

            binary_str = str(remainder) + binary_str

            the_int_val  = the_int_val//2
        print(binary_str)

deci_convert()
        


