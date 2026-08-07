def bubbleSort(element,keys=None):
    # Outer loop uses 'i'
    for i in range(len(element) - 1):
        swapped = False
        
        # Inner loop changed to 'j'
        for j in range(len(element) - 1 - i):
            a = element[j][keys]
            b = element[j + 1][keys]
            if b < a:
                # Swap elements using 'j'
                element[j], element[j + 1]= element[j + 1], element[j]
                swapped = True
        
        if not swapped:
            break


if __name__ == "__main__":
    element = [5,9,2,1,67,34,88,34]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements_dict = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 500,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 700,  'device': 'iphone-8'},
    ]
    # bubbleSort(elements_dict, "name")
    bubbleSort(elements_dict, keys="transaction_amount")
    # bubbleSort(elements)
    # bubbleSort(elements)
    # print(element)
    print(elements_dict)
    # print(elements)
    # print(bubbleSort(element))


