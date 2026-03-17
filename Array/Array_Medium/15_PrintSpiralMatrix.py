def print_spiral(matrix):
    r = len(matrix)
    c = len(matrix[0])

    top = 0
    right = len(matrix[0])-1
    bottom = len(matrix)-1
    left = 0
    res = []

    while top<=bottom and left<=right:
        for i in range(top,right+1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top,bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left += 1

    return res


nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(print_spiral(nums))
