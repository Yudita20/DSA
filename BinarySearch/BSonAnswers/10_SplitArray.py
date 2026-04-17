def subarray_max(nums , k):
    count = 1
    sum_subarray= 0

    for x in nums:
        if sum_subarray + x <= k:
            sum_subarray += x
        else:
            count += 1
            sum_subarray = x

    return count

def split_array_k(nums , k):
    if len(nums) < k:
        return -1

    low , high = max(nums) , sum(nums)
    while low <= high:
        mid = (low + high) // 2

        if subarray_max(nums , mid) > k:
            low = mid + 1
        else:
            high = mid - 1

    return low


arr = [1,2,3,4,5]
print(split_array_k(arr , 3))