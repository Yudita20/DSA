def kadane_max(arr):
    curr_sum = 0
    max_sum = float("-inf")

    for i in range(len(arr)):
        curr_sum = max(arr[i],curr_sum+arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

def kadane_min(arr):
    curr_sum = 0
    min_sum = float("+inf")

    for i in range(len(arr)):
        curr_sum = min(arr[i],curr_sum+arr[i])
        min_sum = min(min_sum, curr_sum)
    return min_sum

def maximum_circular_sum(arr):
    n = len(arr)
    # Find total sum
    total_sum = sum(arr)

    # Find min subarray sum
    min_sum = kadane_min(arr)

    # Find max subarray sum
    max_sum = kadane_max(arr)

    # Find circular sum
    circular_sum = total_sum - min_sum

    # return max_sum
    if max_sum>0:
        # If array contains only negative values
        return max(max_sum,circular_sum)
    return max_sum


nums = [5,-3,5]
print(maximum_circular_sum(nums))