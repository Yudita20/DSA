"""
Given an integer array nums, return true if nums is consecutive, otherwise return false.

An array is consecutive if it contains every number in the range [x, x + n - 1] (inclusive),
where x is the minimum number in the array and n is the length of the array.

Example:
    Input: nums = [1,3,4,2]
    Output: true

    Explanation:
    The minimum value is 1 and the length of nums is 4.
    All the values in the range [x, x + n - 1] = [1, 1 + 4 - 1] = [1, 4] = (1, 2, 3, 4) occur in nums.
    Therefore, nums is consecutive.
"""


def consecutiveArray(nums):
    min_elt = min(nums)
    max_elt = max(nums)

    if (max_elt - min_elt + 1) != len(nums):
        return False

    set_value = set()

    for i in nums:
        if i in set_value:
            return False
        else:
            set_value.add(i)

    calculated_range = max_elt - min_elt + 1
    for j in range(min_elt, calculated_range):
        if j + 1 not in set_value:
            return False

    return True

def checkConsecutive(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            return False

    return True

if __name__ == "__main__":
    arr = [1,3,2,4]
    print(consecutiveArray(arr))
    print(checkConsecutive(arr))