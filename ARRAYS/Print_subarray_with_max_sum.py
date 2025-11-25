def PrintSubarray(nums):
    curr_sum = 0
    max_sum = float("-inf")
    start_index = -1
    end_index = -1
    start = 0
    for i in range(0 , len(nums)):
        if curr_sum == 0:
            start = i

        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start_index = start
            end_index = i

        if curr_sum < 0:
            curr_sum =0

    for i in range(start_index , end_index+1):
        print(nums[i], end=" ")

num = [-2,1,-3,4,-1,2,1,-5,4]
PrintSubarray(num)