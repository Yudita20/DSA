def occurrence(arr,tar):
    i = 0
    j = len(arr)-1
    s , e = -1 , -1

    while i <= j and  arr[i] != tar:
        i += 1

    while i <= j and arr[j] != tar:
        j -= 1

    if i > j:
        return [-1,-1]
    else:
        return [i,j]


def occur(arr,tar):
    s , e = 0 , len(arr)-1
    i , j = -1 , -1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == tar:
            i = j = mid
            while i > 0 and arr[i-1] == tar:
                i -= 1
            while j < len(arr) and arr[j+1] == tar:
                j += 1
            return [i,j]
        elif arr[mid] < tar:
            s = mid + 1
        else:
            e = mid - 1

    return [i,j]

def lb(nums, tar):
    s, e = 0, len(nums) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if nums[mid] >= tar:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans

def up(nums, tar):
    s, e = 0, len(nums) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if nums[mid] <= tar:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1
    return ans

def searchRange(nums, target):
    lower = lb(nums, target)
    upper = up(nums, target) - 1

    if lower <= upper and nums[lower] == target:
        return [lower, upper]
    return [-1, -1]


nums = [5,7,7,8,8,8,10]
print(occurrence(nums,8))
print(occur(nums,9))
print(searchRange(nums,9))














