# 5_PowerSetBitManipulation

def powerSet(nums):
    n = len(nums)
    result = []

    for i in range(1 << n):
        subsets = []
        for j in range(n):
            if i & (1 << j):
                subsets.append(nums[j])
        result.append(subsets)

    return result


if __name__ == "__main__":
    arr = [1,2,3]
    print(powerSet(arr))