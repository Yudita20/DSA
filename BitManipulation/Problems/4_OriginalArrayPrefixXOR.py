def originalArray(prefix):
    n = len(prefix)
    result = [0] * n

    result[0] = prefix[0]
    for i in range(1, len(prefix)):
        result[i] = prefix[i-1] ^ prefix[i]

    return result


if __name__ == "__main__":
    nums = [5,2,0,3,1]
    print(originalArray(nums))