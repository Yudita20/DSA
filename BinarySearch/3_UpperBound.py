def upper_bound(arr,x):
    start = 0
    right = len(arr)-1
    ans = len(arr)

    while start <= right:
        mid = (start + right)//2

        if arr[mid] <= x:
            start = mid+1
        else:
            ans = mid
            right = mid-1

    return ans

nums = [3,5,8,15,19]
print(upper_bound(nums,9))
