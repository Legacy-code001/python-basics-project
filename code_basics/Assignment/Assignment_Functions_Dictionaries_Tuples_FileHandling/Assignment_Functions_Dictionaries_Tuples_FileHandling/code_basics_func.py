def customer_anlysis():
    results = {}
    with open("customers.txt", 'r') as f:
        for val in f:
            print(val)

            name, amount = val.strip().split(',')
            results[name] = int(amount)
    return results

print(customer_anlysis())






# 1. Bronze: Total purchases $100-$199
# 1. Silver: Total purchases $200-$499
# 1. Gold: Total purchases $500+
def calculate_rewards(customer_details):
    if int(customer_details) <= 199:
        print(f"Bronze: Total purchases $100-$199")
    elif int(customer_details) <= 499:
        print(f"Silver: Total Purchases $200-$499")
    else:
        print(f"Total purchases $500+")

def customer_summary():
    final = {}
    customer_data = customer_anlysis()
    print(customer_data)

    for key, value in customer_data.items():
        if int(value) >= 500:
            final[key] = (value, 'Gold')
        elif int(value) >= 200:
            final[key] = (value, "Silver")
        elif int(value) >= 100:
            final[key] = (value, "Bronze")
        else:
            final[key] = (value, "None")
    return final

print(customer_summary())

def result_in_file():
    file_name = input("the file: ")
    with open(file_name, 'w') as f:
        write = f.writelines()
        return write




