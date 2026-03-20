def count_subarray_XOR(arr,tar):
    count = 0
    for i in range(len(arr)):
        xor = 0
        for j in range(i , len(arr)):
            xor ^= arr[j]

            if xor == tar:
                count += 1

    return count


def count_subarray(arr,k):
    hash_map = {0:1}
    prefix_xor = 0
    count = 0

    for i in range(len(arr)):
        prefix_xor ^= arr[i]

        tar = prefix_xor ^ k
        if tar in hash_map:
            count += hash_map[tar]

        hash_map[prefix_xor] = hash_map.get(prefix_xor,0)+1
    return count

nums = [5,6,7,8,9]
print(count_subarray_XOR(nums,5))
print(count_subarray(nums,5))




