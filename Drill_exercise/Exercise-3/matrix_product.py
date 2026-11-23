def multiply_matrix(A, B):
    rowA, colA = len(A), len(A[0])
    rowB, colB = len(B), len(B[0])

    if colA != rowB:
        return "column of A must be equal to row of B"


    #initialize the result
    result = [[0 for _ in range(colB)] for _ in range(rowA)]


    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                result[i][j] += A[i][k] * B[k][j]
    return result


matrix_a = [
    [1, 2], [3, 4]
]

matrix_b = [
    [5, 6], [7, 8]
]

# Result should be:
# [ (1*5 + 2*7), (1*6 + 2*8) ] -> [19, 22]
# [ (3*5 + 4*7), (3*6 + 4*8) ] -> [43, 50]
print(multiply_matrix(matrix_a, matrix_b))

 









































# def matrix_multiply(A, B):
#     # Get dimensions
#     rows_A, cols_A = len(A), len(A[0])
#     rows_B, cols_B = len(B), len(B[0])
    
#     # Check if multiplication is valid
#     if cols_A != rows_B:
#         raise ValueError("Columns of A must equal Rows of B!")
        
#     # Initialize the result matrix with zeros
#     # Dimensions will be (rows_A x cols_B)
#     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
#     # 3-Nested Loops for multiplication
#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A): # coordinates the dot product
#                 result[i][j] += A[i][k] * B[k][j]
                
#     return result

# Example Usage:
# matrix_a = [,
#     [3, 4]
# ]

# matrix_b = [,
#     [7, 8]
# ]

# # Result should be:
# # [ (1*5 + 2*7), (1*6 + 2*8) ] -> [19, 22]
# # [ (3*5 + 4*7), (3*6 + 4*8) ] -> [43, 50]
# print(matrix_multiply(matrix_a, matrix_b))

