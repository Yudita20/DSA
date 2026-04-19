def k_elt_sorted_array(num1 , num2 , k):
    i , j = 0 , 0
    count = 0
    elt = -1

    if k<1 or k > len(num1)+len(num2):
        return -1

    while i<len(num1) or j < len(num2):
        if i < len(num1) and (j >= len(num2) or num1[i] <= num2[j]):
            elt = num1[i]
            i += 1
        else:
            elt = num2[j]
            j += 1

        count += 1

        if count == k:
            return elt


def sorted_array_index(num1 , num2 , k):
    if k<1 or k > len(num1)+len(num2):
        return -1

    if len(num1) > len(num2):
        return sorted_array_index(num2 , num1 , k)


    len1 , len2 = len(num1) , len(num2)

    left = max(0 , k-len2)
    right = min(k , len1)

    while left <= right:
        part1 = (left + right) // 2
        part2 = k - part1

        l1 = float("-inf") if part1 == 0 else num1[part1 - 1]
        r1 = float("+inf") if part1 == len1 else num1[part1]

        l2 = float("-inf") if part2 == 0 else num2[part2 - 1]
        r2 = float("+inf") if part2 == len2 else num2[part2]

        if l1 <= r2 and l2 <= r1:
            return max(l1 , l2)
        elif l1 > r2:
            right = part1 - 1
        else:
            left = part1 + 1

arr1 = [2,3,6]
arr2 = [7,9]
print(k_elt_sorted_array(arr1 , arr2 , 4))
print(sorted_array_index(arr1 , arr2 , 4))
