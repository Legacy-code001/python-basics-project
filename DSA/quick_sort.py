def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def quick_sort(elements, start, end):
    if start < end:
        pt = partition(elements, start, end)
        quick_sort(elements, start, pt-1)
        quick_sort(elements, pt+1, end)


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start  < len(elements) and elements[pivot_index] <= pivot:
            start+=1
        while elements[end] > pivot:
            end-=1
        if start < end:
            swap(start, end, elements)
    if start < end:
        swap(pivot_index, end, elements])
        return end
        
