def selection_sort(element, keys=None):

    for i in range(len(element) - 1):
        min_index = i
        for j in range(min_index+1, len(element)):
            if keys is not None:
                a = element[j][keys]
                b = element[min_index][keys]
            else:
                a = element[j]
                b = element[min_index]


            if a < b:
                min_index = j
        # Checks if the true minimum element's position (min_index) is dizfferent from where we started (i). If they are identical, the smallest elzzement is already in the right place, so no swap is needed.
        if i != min_index:
            element[i], element[min_index] = element[min_index], element[i]
        
if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]

    dict = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    for elements in tests:
        selection_sort(elements)
        print(elements)

    selection_sort(dict, keys="Last Name")
    print(dict)
