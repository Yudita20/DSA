def calculate_sum(nums , k ,limit):
    total_sum = 0
    for i in nums:
        total_sum += (i + k - 1) // k

    return total_sum <= limit

def smallest_divisor(nums , limit):
    if len(nums) > limit:
        return -1

    low , high = 1 , max(nums)

    while low <= high:
        mid = (low + high) // 2

        if calculate_sum(nums , mid , limit):
            high = mid - 1
        else:
            low = mid + 1

    return low

arr = [8,4,2,3]
print(smallest_divisor(arr , 10))