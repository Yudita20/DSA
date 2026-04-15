def excepted_number(arr , mid , k):
    count = 0

    for x in arr:
        if x <= mid:
            count += 1

    missing = mid - count
    return missing >= k

def k_positive_number(arr , k):
    low , high = 1 , max(arr)+k

    while low <= high:
        mid = (low + high) // 2

        # rather than using a function use this
        # missing = arr[mid] - (mid+1)
        # then missing < k --->low = mid + 1
        # for this return high+1+k
        if excepted_number(arr , mid , k):
            high = mid - 1
        else:
            low = mid + 1

    return low


nums = [3,5,7,10]
print(k_positive_number(nums , 6))