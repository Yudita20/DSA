def count(arr,target):
    c = 0
    for i in range(len(arr)):
        if arr[i] == target:
            c += 1
    return c

def count2(arr,tar):
    c = 0
    s, e = 0, len(arr) - 1
    i, j = -1, -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == tar:
            i = j = mid
            while i > 0 and arr[i - 1] == tar:
                i -= 1
            while j < len(arr)-1 and arr[j + 1] == tar:
                j += 1
            c = j - i + 1
            return c
        elif arr[mid] < tar:
            s = mid + 1
        else:
            e = mid - 1

    return 0

nums = [0,0,1,1,1,2,3]
print(count(nums,1))
print(count2(nums,1))