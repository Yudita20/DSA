def rotate(matrix):
    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(i+1,c):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(r):
        matrix[i] = matrix[i][::-1]

    return matrix
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(nums))