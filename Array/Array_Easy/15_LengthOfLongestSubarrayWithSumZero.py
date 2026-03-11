def longest_lengthSubarray(arr):
    hash_map = {}
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == 0:
            max_len = i + 1

        else:
            if curr_sum in hash_map:
                length = i - hash_map[curr_sum]
                max_len = max(length,max_len)

            else:
                hash_map[curr_sum] = i

    return max_len

nums = [9,-3,3,-1,6,-5]
print(longest_lengthSubarray(nums))