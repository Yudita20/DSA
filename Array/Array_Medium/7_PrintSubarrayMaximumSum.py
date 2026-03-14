def subarray_with_maxSum(arr):
    start = -1
    start_idx = -1
    end_idx = -1
    curr_sum = 0
    max_sum = float("-inf")
    for i in range(len(arr)):
        if curr_sum == 0:
            start = i
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = max(curr_sum , max_sum)
            start_idx = start
            end_idx = i

        if curr_sum < 0:
            curr_sum = 0

    for i in range(start_idx , end_idx+1):
        print(arr[i],end=" ")

nums = [-1,-3,-2,-4]
subarray_with_maxSum(nums)