def median_sorted_array(nums1 , nums2):
    i = j = 0
    n = len(nums1)
    m = len(nums2)
    res = []

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    while i<n:
        res.append(nums1[i])
        i += 1

    while j < m:
        res.append(nums2[j])
        j +=1

    if len(res) % 2 == 1:
        return res[len(res)//2]
    else:
        median = (res[len(res)//2] + res[len(res)//2 - 1])/2
        return median

def median_of_sorted(n1 , n2):
    i = j = 0
    n = len(n1)
    m = len(n2)
    count = -1
    curr , prev = -1 , -1

    while i<n or j<m:
        prev = curr
        if i <n and (j>=m or n1[i] <= n2[j]):
            curr = n1[i]
            i += 1
        else:
            curr = n2[j]
            j += 1

        count += 1

        total = n+m
        if count == (total // 2):
            if total % 2 == 0:
                return (curr + prev) / 2
            else:
                return curr

def median_of_two_sorted_array(num1 , num2):
    if len(num1) > len(num2):
        return median_of_two_sorted_array(num2 , num1)

    len1 , len2 = len(num1) , len(num2)

    left , right = 0 , len1

    while left <= right:
        part1 = (left + right) // 2
        part2 = (len1 + len2 + 1) // 2 - part1

        l1 = float("-inf") if part1 == 0 else num1[part1 - 1]
        r1 = float("+inf") if part1 == len1 else num1[part1]

        l2 = float("-inf") if part2 == 0 else num2[part2 - 1]
        r2 = float("+inf") if part2 == len2 else num2[part2]

        if l1 <= r2 and l2 <= r1:
            if (len1+len2) % 2 == 0:
                return (max(l1 , l2) + min(r1 , r2)) / 2
            else:
                return max(l1 , l2)
        elif l1 > r2:
            right = part1 - 1
        else:
            left = part1 + 1


arr1 = [2,4,6]
arr2 = [1,3,5]
print(median_sorted_array(arr1 , arr2))
print(median_of_sorted(arr1 , arr2))
print(median_of_two_sorted_array(arr1 , arr2))