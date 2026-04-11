def calculate_total_time(nums , k):
    total_hours = 0
    for bananas in nums:
        total_hours += (bananas + k - 1) // k

    return total_hours

def min_eating_speed(nums , h):
    low , high = 1 , max(nums)

    while low <= high:
        mid = (low + high) //2

        total_hour = calculate_total_time(nums , mid)

        if total_hour <= h:
            high = mid - 1
        else:
            low = mid + 1

    return low


arr = [7,15,6,3]
print(min_eating_speed(arr , 8))
