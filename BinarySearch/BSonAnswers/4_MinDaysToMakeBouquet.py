def consecutive_roses(bloom_days , days , m , k):
    count = 0
    bouquet = 0

    for day in bloom_days:
        if day <= days:
            count += 1
            if count == k:
                bouquet += 1
                count = 0
        else:
            count = 0

    return bouquet >= m

def roses_garden(bloom_days , m , k):
    if len(bloom_days) < m*k:
        return -1

    low , high = min(bloom_days) , max(bloom_days)
    while low <= high:
        mid = (low+high)//2

        if consecutive_roses(bloom_days , mid , m , k):
            high = mid - 1
        else:
            low = mid + 1

    return low

nums = [1,10,3,10,2]
print(roses_garden(nums , 3 , 1))