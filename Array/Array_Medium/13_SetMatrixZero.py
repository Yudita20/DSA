def set_zero(matrix):
    r = len(matrix)
    c = len(matrix[0])
    row_track = [0] * r
    col_track = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1

    for i in range(r):
        for j in range(c):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0

    return matrix


def set_matrix_zero(matrix):
    r = len(matrix)
    c = len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    for i in range(c):
        if matrix[i][0] == 0:
            first_row_zero = True
            break

    for j in range(r):
        if matrix[0][j] == 0:
            first_col_zero = True
            break


    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0


    if first_row_zero:
        for i in range(c):
            matrix[0][i] = 0

    if first_col_zero:
        for j in range(r):
            matrix[j][0] = 0

    return matrix


nums = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zero(nums))






































