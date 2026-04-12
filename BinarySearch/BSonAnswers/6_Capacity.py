def is_possible(nums , days , k):
    total_sum = 0
    required_day = 1

    for i in nums:
        if total_sum + i > k:
            required_day += 1
            total_sum = i
        else:
            total_sum += i

    return required_day <= days


def capacity_to_ship_packages(nums , days):
    low , high = max(nums) , sum(nums)

    while low <= high:
        mid = (low + high) // 2

        if is_possible(nums , days , mid):
            high = mid - 1
        else:
            low = mid + 1

    return low

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(capacity_to_ship_packages(arr , 5))

