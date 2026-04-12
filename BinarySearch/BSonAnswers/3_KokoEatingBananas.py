def calculate_min_hours(nums , k , h):
    total_hours = 0
    for i in nums:
        total_hours += (i+k-1)//k

    return total_hours <= h

def min_eating_speed(nums , h):
    low , high = 1 , max(nums)

    while low <= high:
        mid = (low + high) // 2

        if calculate_min_hours(nums , mid , h):
            high = mid - 1
        else:
            low = mid + 1

    return low


arr = [25, 12, 8, 14, 19]
print(min_eating_speed(arr , 5))
