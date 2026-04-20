def search_brute(matrix , tar):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == tar:
                return True

    return False


def search_better(matrix , tar):
    row = len(matrix)
    col = len(matrix[0])

    i = 0
    while i < row:
        curr_min = matrix[i][0]
        curr_max = matrix[i][col-1]

        if tar > curr_max:
            i += 1
        elif tar < curr_min:
            return False
        else:
            low , high = 0 , col-1
            while low <= high:
                mid = (low+high)//2

                if matrix[i][mid] == tar:
                    return True
                elif matrix[i][mid] > tar:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

    return False

def search_optimal(matrix , tar):
    m = len(matrix)
    n = len(matrix[0])

    low , high = 0 , m * n -1

    while low <= high:
        mid = (low + high) // 2

        row = mid // n
        col = mid % n

        if matrix[row][col] == tar:
            return True
        elif matrix[row][col] > tar:
            high = mid - 1
        else:
            low = mid + 1

    return False


nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(search_brute(nums , 8))
print(search_better(nums , 14))
print(search_optimal(nums , 19))

