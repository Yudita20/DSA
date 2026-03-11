def subarray(arr , k):
    curr_sum = 0
    count = 0
    hash_map = {0:1}

    for num in arr:
        curr_sum += num

        present = curr_sum - k
        if present in hash_map:
            count += hash_map[present]
        hash_map[curr_sum] = hash_map.get(curr_sum , 0) + 1

    return count

nums = [-1,1]
print(subarray(nums,0))

