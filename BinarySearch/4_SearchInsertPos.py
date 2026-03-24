def search(arr,k):
    s = 0
    e = len(arr)-1

    while s <= e:
        mid = (s+e)//2

        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            e = mid-1

        else:
            s = mid+1

    return s

nums = [1,3,5,6]
print(search(nums,2))
