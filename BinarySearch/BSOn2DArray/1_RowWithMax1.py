def row_with_max_one_brute(matrix):
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    idx = -1

    for i in range(row):
        curr_count = 0
        for j in range(col):
            if matrix[i][j] == 1:
                curr_count += 1


        if curr_count > count:
            count = curr_count
            idx = i

        elif curr_count == count and idx != -1:
            idx = min(idx , i)

    return idx

def row_max_one_better(matrix):
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    idx = -1

    for i in range(row):
        first_one = col
        low, high = 0, col - 1
        while low <= high:
            mid = (low + high) // 2

            if matrix[i][mid] == 1:
                first_one = mid
                high = mid - 1
            else:
                low = mid + 1

        curr_count = col - first_one

        if curr_count > count:
            count = curr_count
            idx = i

    return idx


nums = [[1,0,0],[0,1,1],[1,0,0]]
print(row_with_max_one_brute(nums))
print(row_max_one_better(nums))