def count_each_row(arr , num):
    low , high = 0 , len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= num:
            low = mid + 1
        else:
            high = mid - 1
    return low

def matrix_median(matrix):
    row = len(matrix)
    col = len(matrix[0])

    median = (row * col)//2 + 1

    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    while low <= high:
        mid = (low + high) // 2

        count = 0

        for r in matrix:
            count += count_each_row(r , mid)

        if count < median:
            low = mid + 1
        else:
            high = mid - 1

    return low

nums = [[1,3,8],[2,3,4],[1,2,5]]
print(matrix_median(nums))
