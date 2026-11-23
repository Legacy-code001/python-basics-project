def longest_consecutive(number):
    num_dict = {}
    max_len = 0

    for num in number:
        if num in num_dict:
            continue

        left_length = num_dict.get(num - 1, 0)
        right_length = num_dict.get(num + 1, 0)

            # cumm_num = num
            # max_len = 1

        current_length = left_length + right_length + 1
        num_dict[num] = current_length


        num_dict[num - left_length] = current_length
        num_dict[num + right_length] = current_length

        if current_length > max_len:
            max_len = current_length

    return max_len

print(longest_consecutive([100, 4, 200, 1, 3, 2]))








# def longest_consecutive_boundary(nums):
#     # Dictionary to map a boundary number to its current sequence length
#     num_lengths = {}
#     max_len = 0
    
#     for num in nums:
#         # Skip duplicates to avoid messing up interval calculations
#         if num in num_lengths:
#             continue
            
#         # Check the lengths of adjacent sequences
#         left_len = num_lengths.get(num - 1, 0)
#         right_len = num_lengths.get(num + 1, 0)
        
#         # Total length of the new merged sequence
#         current_len = left_len + right_len + 1
        
#         # Mark the current number as visited (any dummy value works, but we use current_len)
#         num_lengths[num] = current_len
        
#         # Update the outermost boundaries of this sequence
#         num_lengths[num - left_len] = current_len
#         num_lengths[num + right_len] = current_len
        
#         if current_len > max_len:
#             max_len = current_len
            
#     return max_len
# print(longest_consecutive[100, 4, 200, 1, 3, 2])