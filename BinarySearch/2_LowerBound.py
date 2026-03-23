def lower_bound(arr,x,start,end):
    ans = len(arr)

    start , end = 0 , len(arr)-1
    while start <= end:
        mid = (start+end)//2

        if arr[mid] >= x:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

nums = [3,5,8,15,19]
print(lower_bound(nums,9,0,len(nums)-1))



