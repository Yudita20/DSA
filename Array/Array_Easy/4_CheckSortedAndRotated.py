def sorted_and_rotated(nums):
    # T(n) : O(n)
    # S(n) : O(1)

    #APPROACH
    # If the array is sorted and rotated, the order will break at one point or
    # at no point if array is sorted but not rotated

    count = 0
    n = len(nums)

    for i in range(len(nums)):
        if nums[i] > nums[(i+1)%n]:
            count += 1

    if count <= 1:
        return True
    else:
        return False


arr = [3,4,5,1,2]
print(sorted_and_rotated(arr))