def pascalTriangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1]*(i+1)

        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


def pascal(r,c):
    if c==1 or r == c:
        return 1

    return pascal(r-1,c-1) + pascal(r-1,c)


# 0th based indexing
def find_nth_row(row_index):
    res = []
    val = 1
    res.append(val)

    for i in range(1,row_index+1):
        val = val * (row_index - i + 1)//i
        res.append(val)

    return res


print(pascalTriangle(5))
print(pascal(5,4))
print(find_nth_row(4))