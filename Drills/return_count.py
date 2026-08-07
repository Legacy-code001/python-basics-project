
def count_up(n):
    result_list = []
    if n < 1:
        return result_list
    else:
        for i in range(1, n + 1):
            result_list.append(i)
        return result_list

print(count_up(20))
# print(result_list)
    
