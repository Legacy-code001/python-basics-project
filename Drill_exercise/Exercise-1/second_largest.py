def sec_large(list_num):
    n = len(list_num)
    # Edge case: list must have at least 2 elements
    if n < 2:
        return None 
        
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if list_num[j] > list_num[j + 1]:
                # Correct tuple swapping syntax
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
                swapped = True
                
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
            
    # Return the second to last element
    return list_num[-2]

if __name__ == "__main__":
    list_num = [10, 5, 8, 20, 15]
    print(sec_large(list_num))  # Output: 15






