def longestSubarray(nums , k):
    length = 0
    for i in range(0 , len(nums)):
        for j in range(i,len(nums)):
            sum = 0
            for k in range(i , j+1):
                sum += nums[k]
            if sum == k:
                length = max(length , j-i+1)
    return length

def longestSubarray2(nums , k):
    length = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                length = max(length , j-i+1)
    return length

def longestSubarrayWithSumk(nums , k):
    prefix_sum = 0
    length = 0
    hash_map = {0:-1}
    for i in range(0 , len(nums)):
        prefix_sum += nums[i]
        rem  = prefix_sum - k
        if rem in hash_map:
            length = max(length , i-hash_map[prefix_sum - k])
        if rem not in hash_map:
            hash_map[prefix_sum] = i
    return length


def longestSubarrayTwoPointer(nums , k):
    i = j = 0
    prefix_sum = nums[0]
    max_len = 0
    while j <len(nums):
        while i <= j and prefix_sum > k:
            prefix_sum -= nums[i]
            i += 1

        if prefix_sum == k:
            max_len = max(max_len , j-i+1)

        j+=1

        if j<len(nums):
            prefix_sum += nums[j]

    return max_len
# num = [1,2,3,1,1,3]
# num = [2,3,5,1,9]
# num = [2,3,5]
num = [1,2,1,1,1,4]
k1 = 5
print(longestSubarray(num , k1))
print(longestSubarray2(num , k1))
print(longestSubarrayWithSumk(num , k1))
print(longestSubarrayTwoPointer(num , k1))
















