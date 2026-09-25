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


if __name__ == "__main__":
    arr1 = [2,2,3,3,1]
    print(singleNumberI(arr1))

    arr2 = [2,3,2,2]
    print(singleNumberII(arr2))
