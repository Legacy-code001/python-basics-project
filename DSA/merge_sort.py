
def merge_unsort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_unsort(left)
    merge_unsort(right)

    merge_sort(left, right, arr)


def merge_sort(a,b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


if __name__ ==  "__main__":
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    
    for arr in test_cases:
        merge_unsort(arr)
        print(arr)