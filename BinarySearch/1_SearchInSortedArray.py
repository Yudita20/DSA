def binary_search(arr,target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return -1

def recursive_binarySearch(arr,start,end,target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binarySearch(arr, start, mid - 1, target)
    else:
        return recursive_binarySearch(arr, mid + 1, end, target)


nums = [-1,1,4,6,8,10,11]
print(binary_search(nums,9))
print(recursive_binarySearch(nums,0,len(nums)-1,9))