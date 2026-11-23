def subArray(nums: list[int]) -> int :
    if not nums:
        return 0, (-1, -1)
    max_val = nums[0]
    current_sum = nums[0]


    best_start = 0
    best_end = 0

    current_index = 0

    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            current_index = i
        else:
            current_sum += nums[i]

        if current_sum > max_val:
            max_val = current_sum
            best_start = current_index
            best_end = i
    return max_val, (best_start, best_end)

print(subArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    

