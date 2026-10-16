transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]

def get_income(transactions):
    cumm = 0
    for val in transactions:
        if val["type"] == "income":
            cumm += val["amount"]
    return cumm

def get_expenses(transactions):
    return sum(val["amount"] for val in transactions if val["type"] == "expense")
    # cummExp = 0
    # for val in transactions:
    #     if val["type"] == "expense":
    #         cummExp += val["amount"]
    # return cummExp
def calculate_total(transactions):
    comm = 0
    for val in transactions:
        comm = comm + val["amount"]
    return comm

def balance():
    return get_income(transactions) - get_expenses(transactions)
    

def larger_expenses(transactions):
    large_expense = 0
    for val in transactions:
        if val["type"] == "expense":
            if val["amount"] > large_expense:
                large_expense = val["amount"]
    return large_expense

def num_of_expenses(transactions):
    count = 0
    for val in transactions:
        if val["type"] == "expense":
            count+=1
    return count

def analyse_transaction():
    print(f"total incone: {get_income(transactions)}")
    print(get_expenses(transactions))
    print(calculate_total(transactions))
    print(balance())
    print(larger_expenses(transactions))
    print(num_of_expenses(transactions))
    return
analyse_transaction()



    




