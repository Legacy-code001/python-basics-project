"""
Insertion Sort: Divides the array into virtual sorted and unsorted segments. It takes elements from the unsorted part one by one and shifts elements to slide it into its correct position inside the sorted part

"""


# def insertion(element):
#     for i in range(len(element)):
#         anchor = element[i]
#         j = i - 1
#         while j >= 0 and anchor < element[j]:
#             element[j + 1] = element[j]
#             j = j - 1
#         element[j + 1] = anchor

# def insertion(element):
#     for i in range(len(element)):
#         res = []
#         # anchor = element[i]
#         j = i - 1
#         while j >= 0 and anchor < element[j]:
#             element[j + 1] = element[j]
#             res.append((element[j + 1] + element[j])/2)
#             j = j - 1
#         element[j + 1] = anchor
#         res.append((element[j + 1] + anchor)/2)


# if __name__ == '__main__':
#     elements = [11,9,29,7,2,15,28]
#     insertion(elements)
#     print(elements)


def print_running_medians(sequence):
    # This list will hold the elements sorted in real-time
    sorted_list = []
    
    for element in sequence:
        # Step 1: Insert the new element into its correct sorted position
        # (This mimics one complete pass of an insertion sort)
        sorted_list.append(element)
        i = len(sorted_list) - 1
        anchor = sorted_list[i]
        j = i - 1
        
        while j >= 0 and anchor < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = anchor
        
        # Step 2: Compute the median of the sorted list so far
        n = len(sorted_list)
        mid = n // 2
        
        if n % 2 == 1:
            # Odd number of elements: pick the single middle element
            median = float(sorted_list[mid])
        else:
            # Even number of elements: average the two middle elements
            median = (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
            
        print(median)

# Test execution
if __name__ == '__main__':
    stream = [2, 1, 5, 7, 2, 0, 5]
    print_running_medians(stream)
