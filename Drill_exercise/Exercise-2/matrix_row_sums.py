def sum_matrix(the_matrix):
    len_matrix = len(the_matrix)
    for row in range(len_matrix):
        row_cumm = 0
        each_row = the_matrix[row]
        for j in range(len(each_row)):
            row_cumm += each_row[j]
        print(f"Row {row + 1} total: {row_cumm}")


sum_matrix([[2,4,6], [1,3,5], [10, 20, 30]])







