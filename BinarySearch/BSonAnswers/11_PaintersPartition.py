def painters_count(nums , mid , b):
    count = 1
    time = 0

    for x in nums:
        if time + x*b <= mid:
            time += x*b
        else:
            count += 1
            time = x*b

    return count

def painters_partition(nums , a , b):
    low = max(nums)*b
    high = sum(nums)*b

    while low <= high:
        mid = (low + high)//2
        if painters_count(nums , mid , b) > a:
            low = mid + 1

        else:
            high = mid - 1

    return low


arr = [1,10]
print(painters_partition(arr , 2 , 5))