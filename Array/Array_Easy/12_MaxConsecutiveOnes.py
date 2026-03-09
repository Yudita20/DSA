def maximum_ones(arr):
    count = 0
    max_count = float("-inf")

    for i in range(1,len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)

    return max_count


nums = [0,0,0,0,0,0,0]
print(maximum_ones(nums))