def can_place_cows(stalls , mid , k):
    count = 1
    last_placed = stalls[0]

    for i in range(1 , len(stalls)):
        if stalls[i] - last_placed >= mid:
            count += 1
            last_placed = stalls[i]

        if count >= k:
            return True

    return False

def aggressive_cows(stalls , k):
    stalls.sort()

    low , high = 0 , stalls[-1] - stalls[0]
    ans = 0

    while low <= high:
        mid = (low + high)//2

        if can_place_cows(stalls , mid , k):
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    return ans

nums = [0,3,7,10,9]
print(aggressive_cows(nums , 4))
