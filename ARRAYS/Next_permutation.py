def nextPermutation(nums):
    index = -1
    for i in range(len(nums)-1 , -1 , -1):
        if nums[i-1] < nums[i]:
            index = i-1
            break

    if index == -1:
        nums.reverse()
        return

    for i in range(len(nums) - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index + 1:] = reversed(nums[index + 1:])
    return nums[:]


num = [1,3,2]
print(nextPermutation(num))