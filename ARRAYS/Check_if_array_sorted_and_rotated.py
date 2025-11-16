def isSortedAndRotated(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    return count <= 1


num = [1,1,1]
print(isSortedAndRotated(num))