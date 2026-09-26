def singleNumberI(nums):
    xor = 0
    for i in nums:
        xor ^= i

    return xor

def singleNumberII(nums):
    result = 0
    for k in range(0, 32):
        bit_sum = 0

        for num in nums:
            if num < 0:
                num = num & (2**31 - 1)
            bit_sum += (num >> k) & 1

        bit_sum %= 3
        result = result | bit_sum << k

    return result

def singleNumberIII(nums):
    xor_r = 0

    for num in nums:
        xor_r ^= num

    mask = xor_r & (-xor_r)

    group_a = 0
    group_b = 0

    for num in nums:
        if num & mask != 0:
            group_a ^= num
        else:
            group_b ^= num

    return [group_a, group_b]

if __name__ == "__main__":
    # arr1 = [2,2,3,3,1]
    # print(singleNumberI(arr1))
    #
    # arr2 = [2,3,2,2]
    # print(singleNumberII(arr2))

    arr = [1,2,1,3,5,2]
    print(singleNumberIII(arr))
