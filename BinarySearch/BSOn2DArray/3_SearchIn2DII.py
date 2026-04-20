def search_optimal(matrix , tar):
    m = len(matrix)
    n = len(matrix[0])

    row , col = 0 , n-1

    while row < m  and col >= 0:
        if matrix[row][col] == tar:
            return True
        elif matrix[row][col] > tar:
            col -= 1
        else:
            row += 1

    return False


nums = [[1,2,3,4,5],[6,7,8,9,10]]
print(search_optimal(nums , 11))