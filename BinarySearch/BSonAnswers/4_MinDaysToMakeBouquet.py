def is_possible(arr , days , m , k):
    count = 0
    bouquet = 0

    for day in nums:
        if day <= days:
            count += 1

            if count == k:
                bouquet += 1
                count = 0
        else:
            count = 0

    return bouquet >= m


def roses_garden(arr , m , k):
    if len(arr) < m * k:
        return 0

    low , high = min(arr) , max(arr)

    while low <= high:
        mid = (low + high) // 2

        if is_possible(arr , mid , m , k):
            high = mid - 1
        else:
            low = mid + 1
    return low


nums = [1,10,3,10,2]
print(roses_garden(nums , 3 , 1))

